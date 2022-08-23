#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - Checks if a singly-linked list contains a cycle.
 * @list: A singly-linked list.
 *
 * Return: If there is no cycle - 0.
 *         If there is a cycle - 1.
 */
int check_cycle(listint_t *list)
{
	listint_t *list_slow, *list_fast;

	if (list == NULL || list->next == NULL)
		return (0);


	list_slow = list->next;
	list_fast = list->next->next;
	while (list_slow && list_fast && list_fast->next)
	{
		if (list_slow == list_fast)
			return (1);
		list_slow = list_slow->next;
		list_fast = list_fast->next->next;
	}

	return (0);
}
