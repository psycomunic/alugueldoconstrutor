# -*- coding: utf-8 -*-
"""JSON-LD (schema.org).

Tudo sai de um @graph por pagina, com @id estaveis para os nos que se repetem
(Organization, WebSite, cada unidade). Assim o Google entende que a
"Organization" citada em 27 paginas e sempre a mesma entidade.

O que NAO fazemos aqui, de proposito:
  - Review / AggregateRating da propria empresa no proprio site. O Google trata
    isso como "self-serving review" e pode aplicar penalidade manual.
  - Offer com preco. Nao temos tabela publica; preco inventado e pior que
    nenhum preco.
  - geo com latitude/longitude. Nao temos as coordenadas confirmadas.
    Enquanto isso usamos hasMap, que e verificavel.
"""
import json

import partials as P
from content import EQUIPAMENTOS, UNIDADES, FAQ_GERAL

ORG_ID = P.SITE + "/#organization"
SITE_ID = P.SITE + "/#website"


def dumps(objs):
    graph = objs if isinstance(objs, list) else [objs]
    data = {"@context": "https://schema.org", "@graph": graph}
    return ('<script type="application/ld+json">%s</script>'
            % json.dumps(data, ensure_ascii=False, separators=(",", ":")))


# --------------------------------------------------------------------- base
def organization():
    return {
        "@type": ["Organization", "LocalBusiness"],
        "@id": ORG_ID,
        "name": P.BRAND,
        "legalName": P.LEGAL,
        "taxID": P.CNPJ,
        "vatID": P.CNPJ,
        "url": P.SITE + "/",
        "logo": {
            "@type": "ImageObject",
            "url": P.SITE + "/assets/img/logo-mark.png",
            "width": 512, "height": 512,
        },
        "image": P.SITE + "/assets/img/og-cover.jpg",
        "description": ("Locação de equipamentos para construção civil no Rio de Janeiro: "
                        "andaimes, betoneiras, marteletes, compactadores, escoras e mais. "
                        "Cinco unidades e entrega com frota própria."),
        "slogan": "Tudo para sua obra",
        "telephone": P.PHONE_TEL,
        "address": {
            "@type": "PostalAddress",
            "streetAddress": UNIDADES[0]["rua"],
            "addressLocality": P.CITY,
            "addressRegion": P.STATE,
            "addressCountry": P.COUNTRY,
        },
        "areaServed": [{"@type": "City", "name": "Rio de Janeiro"}] +
                      [{"@type": "Place", "name": a} for a in P.AREAS],
        "sameAs": [P.INSTAGRAM, P.FACEBOOK],
        "contactPoint": [{
            "@type": "ContactPoint",
            "contactType": "customer service",
            "telephone": P.PHONE_TEL,
            "availableLanguage": ["Portuguese"],
            "areaServed": "BR",
        }],
        "openingHoursSpecification": _hours(),
        "knowsAbout": ["locação de andaimes", "locação de betoneiras",
                       "locação de marteletes", "escoramento de laje",
                       "equipamentos para construção civil"],
        "department": [{"@id": _unit_id(u)} for u in UNIDADES],
    }


def _hours():
    return [
        {"@type": "OpeningHoursSpecification",
         "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
         "opens": "07:00", "closes": "17:00"},
        {"@type": "OpeningHoursSpecification",
         "dayOfWeek": ["Saturday"], "opens": "07:00", "closes": "12:00"},
    ]


def website():
    return {
        "@type": "WebSite",
        "@id": SITE_ID,
        "url": P.SITE + "/",
        "name": P.BRAND,
        "inLanguage": "pt-BR",
        "publisher": {"@id": ORG_ID},
    }


def webpage(path, name, description, breadcrumb_id=None, primary_image=None, page_type="WebPage"):
    o = {
        "@type": page_type,
        "@id": P.url(path) + "#webpage",
        "url": P.url(path),
        "name": name,
        "description": description,
        "isPartOf": {"@id": SITE_ID},
        "about": {"@id": ORG_ID},
        "inLanguage": "pt-BR",
    }
    if breadcrumb_id:
        o["breadcrumb"] = {"@id": breadcrumb_id}
    if primary_image:
        o["primaryImageOfPage"] = {"@type": "ImageObject",
                                   "url": P.SITE + "/" + primary_image.lstrip("/")}
    return o


def breadcrumb(path, trail):
    """trail: lista de (href|None, label), a mesma passada para partials.crumbs."""
    items = []
    for i, (href, label) in enumerate(trail, start=1):
        it = {"@type": "ListItem", "position": i, "name": label}
        if href:
            it["item"] = P.url(href)
        items.append(it)
    return {
        "@type": "BreadcrumbList",
        "@id": P.url(path) + "#breadcrumb",
        "itemListElement": items,
    }


def faqpage(path, pares):
    return {
        "@type": "FAQPage",
        "@id": P.url(path) + "#faq",
        "mainEntity": [{
            "@type": "Question",
            "name": q,
            "acceptedAnswer": {"@type": "Answer", "text": a},
        } for q, a in pares],
    }


# --------------------------------------------------------------------- unidades
def _unit_id(u):
    return P.url("unidades/%s.html" % u["slug"]) + "#unidade"


def unidade(u, full=True):
    o = {
        "@type": "LocalBusiness",
        "@id": _unit_id(u),
        "name": "%s - %s" % (P.BRAND, u["nome"]),
        "branchOf": {"@id": ORG_ID},
        "parentOrganization": {"@id": ORG_ID},
        "url": P.url("unidades/%s.html" % u["slug"]),
        "telephone": "+" + u["wa"],
        "address": {
            "@type": "PostalAddress",
            "streetAddress": u["rua"],
            "addressLocality": P.CITY,
            "addressRegion": P.STATE,
            "addressCountry": P.COUNTRY,
        },
        "hasMap": P.maps_link(u["endereco"]),
        "openingHoursSpecification": _hours(),
        "areaServed": [{"@type": "Place", "name": a} for a in u["atende"]],
        "image": P.SITE + "/assets/img/og-cover.jpg",
    }
    if full:
        o["description"] = u["sobre"]
        o["makesOffer"] = [{
            "@type": "Offer",
            "itemOffered": {"@type": "Service", "name": "Locação de %s" % e["nome"].lower()},
        } for e in EQUIPAMENTOS[:8]]
    return o


# --------------------------------------------------------------------- equipamentos
def _eq_id(e):
    return P.url("equipamentos/%s.html" % e["slug"]) + "#servico"


def equipamento(e):
    return {
        "@type": "Service",
        "@id": _eq_id(e),
        "name": "Locação de %s no Rio de Janeiro" % e["nome"].lower(),
        "serviceType": "Locação de %s" % e["nome"].lower(),
        "alternateName": e.get("sinonimos", []),
        "description": e["desc"],
        "url": P.url("equipamentos/%s.html" % e["slug"]),
        "image": P.SITE + "/assets/img/equipamentos/%s.webp" % e["slug"],
        "provider": {"@id": ORG_ID},
        "areaServed": [{"@type": "City", "name": "Rio de Janeiro"}] +
                      [{"@type": "Place", "name": a} for a in P.AREAS[:12]],
        "audience": {"@type": "Audience",
                     "audienceType": "Construtoras, empreiteiros, profissionais autônomos e proprietários em obra"},
        "termsOfService": "Locação por diária, semana, quinzena ou mês.",
        "offers": {
            "@type": "Offer",
            "availability": "https://schema.org/InStock",
            "url": P.url("equipamentos/%s.html" % e["slug"]),
            "seller": {"@id": ORG_ID},
            "areaServed": {"@type": "City", "name": "Rio de Janeiro"},
        },
    }


def catalogo(path):
    """ItemList da pagina hub de equipamentos."""
    return {
        "@type": "ItemList",
        "@id": P.url(path) + "#lista",
        "name": "Equipamentos para locação",
        "numberOfItems": len(EQUIPAMENTOS),
        "itemListElement": [{
            "@type": "ListItem",
            "position": i,
            "name": "Locação de %s" % e["nome"].lower(),
            "url": P.url("equipamentos/%s.html" % e["slug"]),
        } for i, e in enumerate(EQUIPAMENTOS, start=1)],
    }


def lista_unidades(path):
    return {
        "@type": "ItemList",
        "@id": P.url(path) + "#unidades",
        "name": "Unidades do Aluguel do Construtor no Rio de Janeiro",
        "numberOfItems": len(UNIDADES),
        "itemListElement": [{
            "@type": "ListItem",
            "position": i,
            "name": u["nome"],
            "url": P.url("unidades/%s.html" % u["slug"]),
        } for i, u in enumerate(UNIDADES, start=1)],
    }
