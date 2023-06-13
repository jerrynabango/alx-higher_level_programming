#include <Python.h>

/**
 * print_python_list_info - Function that prints basic info about Python lists
 *
 * @p: PyObject
 *
 * Return: Nothing
 */
void print_python_list_info(PyObject *p)
{
	int alloc, list_info = 0, length;
	PyObject *basic_info;
	PyListObject *list = (PyListObject *)p;

	length = Py_SIZE(p);
	alloc = list->allocated;

	printf("[*] Size of the Python List = %d\n", length);
	printf("[*] Allocated = %d\n", alloc);

	while (list_info < length)
	{
		basic_info = PyList_GetItem(p, list_info);
		printf("Element %d: %s\n", list_info, Py_TYPE(basic_info)->tp_name);
		list_info++;
	}
}

