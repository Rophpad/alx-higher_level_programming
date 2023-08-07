#include "lists.h"

/**
 * check_cycle - Checks if a singly-linked list contains a cycle.
 * @list: A singly-linked list.
 *
 * Return: 0 - if cycle doesn't exist
 *         1 - if cycle exist
 */
int check_cycle(listint_t *list)
{
	listint_t **firstNodeAddress = &list;
	listint_t *current;

	if (list == NULL || list->next == NULL)
		return (0);
	current = list->next;
	while (current)
	{
		if (current == *firstNodeAddress)
			return (1);
		current = current->next;
	}
	return (0);
}
