#include "lists.h"

/**
* is_palindrome - A function that checks if a list is a palindrome.
*
* @head: Indicates a pointer to a pointer to a list
*
* Return: 0 if it is not a palindrome, 1 if it is a palindrome
*/
int is_palindrome(listint_t **head)
{
	listint_t *list = *head, *check = *head, *palindrome = NULL, *next;

	if (*head == NULL || (*head)->next == NULL)
	{
		return (1);
	}

	while (check != NULL && check->next != NULL)
	{
		check = check->next->next;
		next = list->next;
		list->next = palindrome;
		palindrome = list;
		list = next;
	}

	if (check != NULL)
	{
		list = list->next;
	}

	for (; palindrome != NULL && list != NULL; palindrome = palindrome->next,
	list = list->next)
	{
		if (palindrome->n != list->n)
		{
			return (0);
		}
	}
	return (1);
}
