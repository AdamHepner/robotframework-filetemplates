import pystache

class FileTemplates:
    ROBOT_LIBRARY_SCOPE = "GLOBAL"
    
    def __init__(self):
        pass

    def render_template(self, template_file, target_file, **parameters):

        with open(template_file, "r") as infile:
            tmpl = infile.read()

        out = pystache.render(tmpl, **parameters)

        with open(target_file, "w") as outfile:
            outfile.write(out)

if __name__ == "__main__":
    infile = "template.tpl"
    outfile = "outfile.py"
    ft = FileTemplates()

    ft.render_template(infile, outfile, testfilename="BigBook0256_process.pdf")