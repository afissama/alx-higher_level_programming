#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
/**
 * insert_node - Insert node in sorted list
 *
 * @head: the node root
 * @number: number to insert
 * Return: listint_t*
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t **list_tmp,  *new, **list_low;

	new = malloc(sizeof(listint_t));
	if (new == NULL || head == NULL)
		return (NULL);

	new->n = number;

	list_tmp = head;
	list_low = head;
	while ((*list_tmp) != NULL && (*list_tmp)->n < number)
	{
		list_low = list_tmp;
		list_tmp = &(*list_tmp)->next;
	}

	if (list_low == list_tmp)
	{
		new->next = (*head);
		(*head) = new;
	}
	else
	{
		new->next = (*list_tmp);
		(*list_low)->next = new;
	}
	return (new);
}
