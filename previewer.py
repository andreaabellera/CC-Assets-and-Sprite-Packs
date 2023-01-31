# Simple script that generates sprite previews for asset pack READMEs

import os
import sys

imgs = ['png','jpg','jpeg','gif']

def isImg(filename):
    toks = filename.split('.')
    return toks[len(toks)-1] in imgs

def main():
    if len(sys.argv) > 1:
        dirname = sys.argv[1]
        path = './' + dirname
        preface = ''
        if(len(sys.argv) > 2):
            preface = sys.argv[2]

        readme = open('./{}/README.md'.format(dirname),'w')

        title = ' '.join(dirname.split('-'))
        readme.write('# ' + title + '\n')
        readme.write(preface + '\n')

        for root, directories, contents in os.walk(path, topdown=True):
            curr_heading = "/"
            for name in contents:
                toks = root.split('\\')
                toks.pop(0)
                heading = '/' + '/'.join(toks)

                if heading != curr_heading:
                    curr_heading = heading
                    readme.write('### ' + heading)

                if isImg(name):
                    shortname = name[:len(name)-4]
                    heading = ""
                    if curr_heading != '/':
                        heading = curr_heading
                    readme.write('![{}](/{}{}/{})\n'.format(shortname,dirname,heading,name))
    else:
        print("Whoops! Please provide an asset directory.\n")


if __name__ == "__main__":
    main()