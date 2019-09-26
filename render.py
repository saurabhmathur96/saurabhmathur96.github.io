#!/usr/bin/env python3


import argparse
from os import path
import json
from bs4 import BeautifulSoup


def read_json(file_path):
	with open(file_path, "r", encoding="utf-8") as infile:
		return json.load(infile)

def render_paper(item):
	links = ['<a class="strong" href="%s">%s</a>' % (link['href'], link['text']) for link in item['links'] ]
	links_html = '&nbsp;&middot;&nbsp;'.join(links)
	published_at = item.get('published_at', '')
	authors = item.get('authors', '')
	return '\n'.join(['<div class="row paper">',
					'<div class="col-sm-3 col-8"><img src="%s" class="img-fluid" alt="%s" /></div>' % (item['img'],item['title']),
					'<div class="col-sm-9">',
					'<a class="strong" href="%s">%s</a>' % (item["source"], item['title']),
					'<p>%s </p>' % ('<br/>'.join(filter(None, [authors, published_at, links_html]))),
					'<p>%s</p>' % item['description'],
					"</div>",
					"</div>"])


def render_project(item):
	links = ['<a class="strong" href="%s">%s</a>' % (link['href'], link['text']) for link in item['links'] ]
	links_html = '&nbsp;&middot;&nbsp;'.join(links)
	published_at = item.get('published_at', '')
	authors = item.get('authors', '')
	return '\n'.join(['<div class="row project">',
					'<div class="col-sm-3 col-8"><img src="%s" class="img-fluid" alt="%s" /></div>' % (item['img'], item['title']),
					'<div class="col-sm-9">',
					'<a class="strong" href="%s">%s</a>' % (item["source"], item['title']),
					'<p>%s </p>' % ('<br/>'.join(filter(None, [authors, published_at, links_html]))),
					'<p>%s</p>' % item['description'],
					"</div>",
					"</div>"])


parser = argparse.ArgumentParser()
parser.add_argument("template_path")
parser.add_argument("--data_dir", default="data")
args = parser.parse_args()

projects_path = path.join(args.data_dir, "projects.json")
projects = read_json(projects_path)
projects_html = '\n'.join([render_project(item) for item in projects])

research_path = path.join(args.data_dir, "research.json")
research = read_json(research_path)
research_html = '\n'.join([render_paper(item) for item in research])


template = open(args.template_path, 'r', encoding="utf8").read()
html = template.replace("[research_html]", research_html).replace("[projects_html]", projects_html)


print (html)