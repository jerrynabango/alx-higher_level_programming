#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/**
 * print_python_list - Function that prints the list of Python objects
 *
 * @p: Indicates a pointer to the pyobject
 */
void print_python_list(PyObject *p)
{
	int i = 0;
	Py_ssize_t len;
	PyObject *object;
	PyListObject *list;

	printf("[*] Python list info\n");

	if (PyList_Check(p))
	{
		list = (PyListObject *)(p);

		len = ((PyVarObject *)(p))->ob_size;
		printf("[*] Size of the Python List = %zu\n", len);
		printf("[*] Allocated = %zu\n", list->allocated);

		while (i < len)
		{
			object = PyList_GET_ITEM(p, i);
			printf("Element %d: %s\n", i, (object->ob_type)->tp_name);
			if (PyBytes_Check(object))
			{
				print_python_bytes(object);
			}
			else if (PyFloat_Check(object))
			{
				print_python_float(object);
			}

			i++;
		}
	}
	else
	{
		printf("  [ERROR] Invalid List Object\n");
	}
}

/**
 * print_python_bytes - Function that prints python bytes
 *
 * @p: Indicates a pointer to the pyobject
 */
void print_python_bytes(PyObject *p)
{
	int i = 0;
	char *buffer;
	Py_ssize_t len;

	printf("[.] bytes object info\n");

	if (PyBytes_Check(p))
	{
		len = PyBytes_Size(p);
		buffer = ((PyBytesObject *)(p))->ob_sval;
		printf("  size: %zu\n", len);
		printf("  trying string: %s\n", buffer);
		if (len > 9)
		{
			len = 9;
		}
		printf("  first %zu bytes: ", len + 1);

		while (i <= len)
		{
			if (i == len)
			{
				printf("%02x\n", buffer[i] & 0xff);
			}
			else
			{
				printf("%02x ", buffer[i] & 0xff);
			}
			i++;
		}
	}
	else
	{
		printf("  [ERROR] Invalid Bytes Object\n");
	}
}

/**
 * print_python_float - Function that prints a float
 *
 * @p: Indicates a pointer to the pyobject
 */
void print_python_float(PyObject *p)
{
	char *py_f = NULL;

	PyFloatObject *float_obj = (PyFloatObject *)p;

	fflush(stdout);

	printf("[.] float object info\n");
	if (strcmp(p->ob_type->tp_name, "float") != 0)
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	py_f = PyOS_double_to_string(float_obj->ob_fval, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", py_f);
	PyMem_Free(py_f);
}

