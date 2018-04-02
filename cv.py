import pystache
import json
import argparse
import sys
import yaml

def render(template, data):
    render = pystache.Renderer()
    parsed = pystache.parse(template)
    res = render.render(parsed, data)
    res = res.encode("utf-8")
    with open("cv.html", 'wb') as fd:
        fd.write(res)


class obj(object):
    pass


def parse():
    args = sys.argv
    parser = None

    args = obj()
    try:
        args.filepath = sys.argv[1]
    except:
        args.filepath = "cv.json"
    try:
        args.formatpaht = sys.argv[2]
    except:
        args.formatpath = "format.json"
    args.temppath = "templates/default_html.mustache"
    print args
    return args


def combine_json(dest, src):
    for key, item in src.iteritems():
        if isinstance(item, dict):
            if key in dest:
                combine_json(item, dest[key])
        else:
            dest[key] = item
    return dest


def main():
    args = parse()
    filepath = args.filepath
    with open(filepath) as fd:
        if filepath.rfind(".json")>=0:
            data = json.load(fd)
        elif filepath.rfind(".yaml")>=0:
            data = yaml.safe_load(fd)

    with open(args.formatpath) as fd:
        format = json.load(fd)

    data = combine_json(data, format)

    with open(args.temppath) as fd:
        template = fd.readlines()
        template = ''.join(template)
        template = template.decode("unicode_escape")

    render(template, data)


if __name__ == '__main__':
    main()
