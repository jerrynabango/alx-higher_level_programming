#include <stdio.h>
#include "/usr/include/python3.4/Python.h"

/**
 * print_python_bytes - A function that prints the bytes
 *
 * @p: Indicates a pointer to the bytes object
 */
void print_python_bytes(PyObject *p)
{
	char *py_list = NULL;
	long int bytes_obj;
	int basic_info = 0;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	PyBytes_AsStringAndSize(p, &py_list, &bytes_obj);
	printf("  bytes_obj: %li\n", bytes_obj);
	printf("  trying string: %s\n", py_list);
	if (bytes_obj < 10)
	{
		printf("  first %li bytes:", bytes_obj + 1);
	}
	else
	{
		printf("  first 10 bytes:");
	}
	while (basic_info <= bytes_obj && basic_info < 10)
	{
		printf(" %02hhx", py_list[basic_info]);
		basic_info++;
	}
	printf("\n");
}

/**
 * print_python_list - A function that prints the list of Python objects
 *
 * @p: Indicates a pointer to the list of Python lists
 */
void print_python_list(PyObject *p)
{
	int python_info = 0;
	const char *type;
	long int bytes_obj = PyList_Size(p);
	PyListObject *list_obj = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %li\n", bytes_obj);
	printf("[*] Allocated = %li\n", list_obj->allocated);
	while (python_info < bytes_obj)
	{
		type = (list_obj->ob_item[python_info])->ob_type->tp_name;
		printf("Element %d: %s\n", python_info, type);
		if (!strcmp(type, "bytes"))
		{
			print_python_bytes(list_obj->ob_item[python_info]);
		}
		python_info++;
	}
}

