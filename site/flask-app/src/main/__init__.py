# -*- coding: utf-8 -*-
import json

from flask import Flask, render_template, Markup
import rdflib

app = Flask(__name__)

supported_languages =  [
    'bar',
#    'ast'
]

languages_data = {}

@app.route("/")
def index():
    for iso in supported_languages:
        if not iso in languages_data:
            rdf = RdfIso(iso)
            (latitude, longitude) = rdf.geo()
            label = rdf.label()
            languages_data[iso] = {
                'label' : label,
                'geo': {
                    'lat': latitude,
                    'lon': longitude
                }
            }
        languages_json = json.dumps(languages_data)

    return render_template('index.html',
        languages_json = Markup(languages_json))

@app.route("/about")
def about():
    return render_template('about.html')

class RdfIso:

    def __init__(self, iso):
        self.g = rdflib.Graph()
        result = self.g.parse(
            "http://glottolog.org/resource/languoid/iso/{0}.rdf".format(iso))
        self.subject = self.g.subjects().next()

    def geo(self):
        latitude = self.g.value(
            self.subject,
            rdflib.term.URIRef(
                u"http://www.w3.org/2003/01/geo/wgs84_pos#lat"))

        longitude = self.g.value(
            self.subject,
            rdflib.term.URIRef(
                u"http://www.w3.org/2003/01/geo/wgs84_pos#long"))

        return (latitude.toPython(), longitude.toPython())

    def label(self):
        name = self.g.value(
            self.subject,
            rdflib.term.URIRef(
                u"http://www.w3.org/2004/02/skos/core#prefLabel"))
        return name.toPython()
