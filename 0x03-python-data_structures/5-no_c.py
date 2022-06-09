#!/usr/bin/env python3

def no_c(my_string):
	res_str = ''.join(i for i in my_string if i not in 'cC')
	return(res_str)
