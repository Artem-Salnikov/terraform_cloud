#!/usr/bin/env python3
import json, yaml, sys, os

def YAMLtoJSON(x):
    with open(x, "r") as (ym):
        ym_dict = yaml.safe_load(ym)
        name_js = (os.path.splitext(os.path.basename(x))[0]) + '.json'
        with open(name_js, 'w') as js:
            js.write(json.dumps(ym_dict, indent=4))

def JSONtoYAML(x):
    with open(x, "r") as (js):
        js_dict = json.load(js)
        name_ym = (os.path.splitext(os.path.basename(x))[0]) + '.yml'
        with open(name_ym, 'w') as ym:
            ym.write(yaml.dump(js_dict, default_flow_style=False, explicit_start=True, explicit_end=True))

def checkYAML(orig_yaml):
    try:
        with open(orig_yaml, "r") as (ym):
            yaml.safe_load(ym)
    except yaml.YAMLError as exc:
        print('Ошибки синтаксиса:')
        print(exc)
        return False
    return True

def checkJSON(orig_json):
    try:
        with open(orig_json, "r") as (js):
            json.load(js)
    except ValueError as exc:
        print ('Ошибки синтаксиса:')
        print(exc)
        return False
    return True

if len(sys.argv) > 1: #Проверка, что скрипту передан параметр в виде пути до файла.
    filename = sys.argv[1]
    if filename.endswith('.json') or filename.endswith('.yml'): #Проверка расширения файла.
        size = os.stat(filename)
        if (size.st_size) > 0: #Проверка, что файл не пустой.
            if filename.endswith('.json') and checkJSON(filename):
                JSONtoYAML(filename)
            elif filename.endswith('.yml') and checkYAML(filename):
                YAMLtoJSON(filename)
        else:
            print('Файл пустой.')
            exit()
    else:
        print ('Неверный формат файла.')
        exit()
else:
    print ('Скрипту не передан входной параметр.')
    exit()


