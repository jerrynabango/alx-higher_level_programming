#include "lists.h"
#include <stddef.h>
#include <stdlib.h>
/**
 * insert_node - function that inserts number into a sorted singly linked list
 *
 * @head: Indicates the pointer to the list element
 *
 * @number: Indicates the integer
 *
 * Return: address of the new node, or NULL if it failed
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *sort1;
	listint_t *sort2 = *head;

	sort1 = malloc(sizeof(listint_t));
	if (sort1 == NULL)
	{
		return (NULL);
	}
	sort1->n = number;

	if (sort2 == NULL || sort2->n >= number)
	{
		sort1->next = sort2;
		*head = sort1;
		return (sort1);
	}

	while (sort2 && sort2->next && sort2->next->n < number)
	{
		sort2 = sort2->next;
	}
	sort1->next = sort2->next;
	sort2->next = sort1;
	return (sort1);
}
