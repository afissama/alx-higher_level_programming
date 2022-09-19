#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * is_palindrome - check if it's palindrom or not
 *
 * @head: list first element
 * Return: int
 */
int is_palindrome(listint_t **head)
{
	size_t len, pos, stop_at;
	listint_t *current, *comp;

	if (head == NULL || *head == NULL)
	{
		return (1);
	}
	len = get_list_length(*head);
	current = *head;
	stop_at = len / 2;
	pos = 0;
	if (len % 2 == 0)
		stop_at--;

	while (current != NULL && pos != stop_at)
	{
		comp = get_node_at_index(*head, (len - 1 - pos));
		if (comp == NULL)
			return (0);
		if (comp->n != current->n)
			return (0);

		current = current->next;
		pos++;
	}

	return (1);
}
