def foo(my_list):
    for i in my_list:
        if i % 2:
            print i
        else:
            break
    else:
        print float('inf')
        
def main():
	foo(list([2,3,4,5,6,7,8,9]))
	
main()