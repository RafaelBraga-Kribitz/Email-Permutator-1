#!/usr/bin/python

'''
	Author: Joseph Dickinson
	05/2014
'''

from optparse import OptionParser

class Permutate:
    """
    Add email providers here.
    """
    email_provider = (
        '@gmail.com',
        '@aol.com',
        '@yahoo.com',
        '@lycos.com'
    )

    def __init__(self):
        self.compute_first_last()

    def compute_first_last(self):
        """
           compute_first_last():
                email_combination = <string> + <string> + <string>
                computes the first name and last name combination plus and email provider.

                Loop through all combinations of first + last + email_provider while the value *is u

                A single combination looks like <fname>.<lname>@<email_provider>
        """
        parser = OptionParser(usage='%prog -f fname -l lname', version='%prog 1.1')

        parser.add_option('-f', '--fname', dest='fname')
        parser.add_option('-l', '--lname', dest='lname')

        (opt, args) = parser.parse_args()

        email_combination = opt.fname + "." + opt.lname
        
        try:
            for provider in Permutate.email_provider:
                print email_combination+provider+","
        except:
            print "Syntax: python permutate_new.py -f <firstname> -l <lastname>] "


    def identify_matches(self):
        """
            identify_matches():
                This method identifies valid emails against the rapportive api.
        """
        


if __name__ == '__main__':
   pm = Permutate()