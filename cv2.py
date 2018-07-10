
import pystache
import json
import argparse
import sys
try:
    import yaml
except:
    pass


def render(template, data):
    render = pystache.Renderer()
    parsed = pystache.parse(template)
    res = render.render(parsed, data)
    res = res.encode("utf-8")
    return res


class obj(object):
    pass


def parse():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--setting", help="", action="store", default="setting.json", type=str, dest="setting")
    parser.add_argument("-d", "--data", help="", action="store", default="cv.json", type=str, dest="data")
    parser.add_argument("-t", "--template", help="", action="store", default="template_html.html", type=str, dest="template")
    parser.add_argument("-l", "--layout", help="", action="store", default="template_html.html", type=str, dest="layout")
    parser.add_argument(nargs=argparse.REMAINDER, dest="value")
    args = parser.parse_args()
    return args


def combine_json(dest, src):
    for key, item in src.iteritems():
        if key in dest:
            if isinstance(item, dict):
                combine_json(item, dest[key])
        else:
            dest[key] = item
    return dest


def main():
    args = parse()
    datafile = args.data
    with open(datafile) as fd:
        if datafile.rfind(".json") >= 0:
            data = json.load(fd)
        elif datafile.rfind(".yaml") >= 0:
            data = yaml.safe_load(fd)

    with open(args.setting) as fd:
        format = json.load(fd)
        

    data = combine_json(data, format)
    s = json.dumps(data, indent=4, sort_keys=True)
    print("setting: \n{}".format(data['settings']))

    with open(args.template) as fd:
        template = fd.readlines()
        template = ''.join(template)
        template = template.decode("unicode_escape")
        res = render(template, data)
        with open("cv.html", 'wb') as fd:
            fd.write(res)

    # with open(args.template) as fd:
    #     template = fd.readlines()
    #     template = ''.join(template)
    #     template = template.decode("unicode_escape")
    #     render(template, data)
    #     with open("detail.html", 'wb') as fd:
    #         fd.write(res)

if __name__ == '__main__':
    main()
