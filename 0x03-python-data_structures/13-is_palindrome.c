#include "lists.h"

/**
 * is_palindrome - A function checks if singly linked list is a palindrome
 *
 * @head: The head of the singly linked list
 *
 * Return: Shows 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *start = NULL;
	listint_t *end = NULL;
	unsigned int list = 0;
	unsigned int list1 = 0;
	unsigned int list2 = 0;
	unsigned int palindrome = 0;

	if (head == NULL)
	{
		return (0);
	}
	else
	{
		return (1);
	}

	start = *head;
	list = list_palindrome(start);
	list1 = list * 2;
	list2 = list1 - 2;
	end = *head;

	while (palindrome < list1)
	{
		if (start[palindrome].n != end[list2].n)
		{
			return (0);
		}
		list2 = list2 - 2;
		palindrome = palindrome + 2;
	}

	return (1);
}

/**
 * check_palindrome - A function that checks for a node
 *
 * @head: Indicates a pointer to a node
 *
 * @index: Indicates a pointer to a node
 *
 * Return: Node from the list of nodes
 */
listint_t *check_palindrome(listint_t *head, unsigned int index)
{
	listint_t *get = head;
	unsigned int node = 0;

	if (head)
	{
		for (get = get; get != NULL; get = get->next)
		{
			if (node == index)
				return (get);

			++node;
		}
	}

	return (NULL);
}

/**
 * list_palindrome - A function that returns elements of a list
 *
 * @integer: Indicates a pointer to a linked list
 *
 * Return: Elements of the list
 */
size_t list_palindrome(const listint_t *integer)
{
	int list_palindrome = 0;

	for (integer = integer; integer != NULL; integer = integer->next)
	{
		++list_palindrome;
	}

	return (list_palindrome);
}