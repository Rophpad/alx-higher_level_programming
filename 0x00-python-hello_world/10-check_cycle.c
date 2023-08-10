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
	listint_t *normal = list;
	listint_t *inAdvance = list;

	while (normal && inAdvance && inAdvance->next)
	{
		normal = normal->next;
		inAdvance = inAdvance->next->next;
		if (normal == inAdvance)
			return (1);
	}

	return (0);
}
