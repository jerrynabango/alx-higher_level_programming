#include "lists.h"

/**
* is_palindrome - function that checks if a list is a palindrome.
* @head: a pointer to pointer
* Return: 1 or 0
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
