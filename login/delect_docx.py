# -*- coding: utf-8 -*-
import os



def delect_docx():

    filepath1 = r'/Users/david/Documents/bello/osr/osr_test/venv/login/cloud_buy.docx'
    filepath2 = r'/Users/david/Documents/bello/osr/osr_test/venv/login/url_candidate.docx'
    filepath3 ='/Users/david/Documents/bello/osr/osr_test/venv/login/url_resume.docx'
    filepath4 ='/Users/david/Documents/bello/osr/osr_test/venv/login/url_third_resume.docx'

    if os.path.exists(filepath1):
        message = 'OK, the "%s" file exists.'
        os.remove('/Users/david/Documents/bello/osr/osr_test/venv/login/cloud_buy.docx')
        print("cloud_buy"+"  delect")
    else:
        message = 'Sorry, I cannot find the "%s" file.'
    if os.path.exists(filepath2):
        message = 'OK, the "%s" file exists.'
        os.remove('/Users/david/Documents/bello/osr/osr_test/venv/login/url_candidate.docx')
        print("url_candidate" + "  delect")
    else:
        message = 'Sorry, I cannot find the "%s" file.'
    if os.path.exists(filepath3):
        message = 'OK, the "%s" file exists.'
        os.remove('/Users/david/Documents/bello/osr/osr_test/venv/login/url_resume.docx')
        print("url_resume" + "  delect")
    else:
        message = 'Sorry, I cannot find the "%s" file.'
    if os.path.exists(filepath4):
        message = 'OK, the "%s" file exists.'
        os.remove('/Users/david/Documents/bello/osr/osr_test/venv/login/url_third_resume.docx')
        print("url_third_resume" + "  delect")
    else:
        message = 'Sorry, I cannot find the "%s" file.'


if __name__ == '__main__':
    delect_docx()

