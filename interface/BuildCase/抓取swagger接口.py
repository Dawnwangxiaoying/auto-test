import requests
import xlwt
import yaml
import os
whitelist = ["config/","/ssfError","download/","wash","/es/","plugininfo/","chat/","documentGeneration/",
             "docautobuilding/","provider/","dataTransfer/","permission/atom","permission/history","permission/engine",
             "permission/syndate","sr/","dataWash/"]
urls = {
    "taskserver": "http://192.168.255.105:9193/taskserver/v2/api-docs"
# {'report':"http://192.168.255.107:8087/report/v2/api-docs"}
       #,"ilaw": "http://192.168.255.105:8080/ilaw/v2/api-docs"}
       #  "judgement": "http://192.168.255.107:9093/judgement-search/v2/api-docs",
       #  "matter": "http://192.168.255.107:9096/matterserver/v2/api-docs",
       #'permission': "http://192.168.255.107:8080/permission/v2/api-docs",
       #  "radar": "http://192.168.255.106:10080/radar/v2/api-docs",

       #  "word": "http://192.168.255.107:10090/officeword/v2/api-docs",
       # "appro":"http://192.168.255.108:8084/appro/v2/api-docs",
       # "book":"http://192.168.255.105:9091/book/v2/api-docs",
       # "cart":"http://192.168.255.105:9093/cart/v2/api-docs",
       # "cnki":"http://192.168.255.106:9090/cnki/v2/api-docs",
       #  "enterprise":"http://192.168.255.106:8088/enterprise/v2/api-docs",
       #  "finance":"http://192.168.255.106:8087/finance/v2/api-docs"
    }


def buildpara(body,definitions):
    parameters = {}
    for para in body:
        if para["in"] == "header":
            break
        else:
            parameters[para["name"]] = "string"

        return parameters


workbook = xlwt.Workbook(encoding = 'ascii')


count = 0
for keys,values in urls.items():


    worksheet = workbook.add_sheet(keys,cell_overwrite_ok=True)
    if 1:
        info = requests.get(values,timeout = 20).json()
        print("正在处理"+keys+"模块接口,共有"+str(len(info["paths"]))+"个子接口")
        index = 0
        definitions = info["definitions"]
        print(definitions)
        for url,values in info["paths"].items():

            isExists = os.path.exists("case/" + keys)
            if not isExists:
                os.makedirs("case/" + keys)

            name = url.replace("/", "_").replace("}", "").replace("{", "").replace("-api", "")[1:]
            flag = 0
            for i in whitelist:
                if i in url:
                    flag = 1
                    break
            if flag == 0:
                singleinfo = {}
                with open("case/" +keys+"/test_"+ name + ".yaml", "w",encoding='utf-8') as yaml_file:
                    singleinfo["url"] = info["basePath"] +  url
                    for method , para in values.items():
                        print(method,para)
                        singleinfo["method"] = method
                        if singleinfo["method"] == "GET":
                            singleinfo["parameters"] = {}
                        else:
                            try:
                                singleinfo["parameters"] = buildpara(para["parameters"],definitions)
                            except:
                                singleinfo["parameters"] = {}

                        singleinfo["contenttype"] = para["consumes"]
                        singleinfo["desc"] = para["summary"]
                    y = yaml.dump(singleinfo,default_flow_style=False,allow_unicode = True)
                    yaml_file.write(y)

                    worksheet.write(index, 0, "N")
                    worksheet.write(index, 2, singleinfo["url"])
                    worksheet.write(index, 5, method)
                    worksheet.write(index, 1, singleinfo["desc"])
                    worksheet.write(index, 3, keys)
                    worksheet.write(index, 6, str(singleinfo["parameters"]))

                    worksheet.write(index, 4, "")
                    index +=1
                    count +=1


                    #for method,intervalues in info.items():




    print("执行完毕，排除白名单共生成" + str(count) + "个yaml文件")

workbook.save('task_Excel_Workbook.xls')

