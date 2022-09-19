#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

listint_t *get_node_at_index(listint_t *head, size_t idx);
size_t get_list_length(const listint_t *h);
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

/**
 * get_list_length - number of nodes
 * @h: pointer to head of list
 * Return: number of nodes
 */
size_t get_list_length(const listint_t *h)
{
	const listint_t *current;
	unsigned int n; /* number of nodes */

	current = h;
	n = 0;
	while (current != NULL)
	{
		current = current->next;
		n++;
	}

	return (n);
}

/**
 * get_node_at_index - Get the node at index object
 *
 * @head:  pointer to pointer of first node of listint_t list
 * @idx: index to access
 * Return: address of the idx th element or NULL if it fails
 */
listint_t *get_node_at_index(listint_t *head, size_t idx)
{
	if (head == NULL || idx == 0)
	{
		return (head);
	}
	if (head->next == NULL)
	{
		return (NULL);
	}
	return (get_node_at_index(head->next, (idx - 1)));
}
