#include "lists.h"

/**
 * is_palindrome - Check is a singly linked list
 * is a palindrome
 * @head: the head of the list
 *
 * Return: 1 if it is palindrome
 *         0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *current;
	int *values;
	bool is_OK = true;
	int i, node_count = 0;

	if (*head == NULL)
		is_OK = true;
	current = *head;
	while (current)
	{
		node_count++;
		current = current->next;
	}
	values = malloc(node_count * sizeof(int));
	current = *head;
	for (i = 0; i < node_count; i++)
	{
		values[i] = current->n;
		current = current->next;
	}
	current = *head;
	for (i = node_count - 1; i >= 0; i--)
	{
		if (current->n != values[i])
		{
			is_OK = false;
			break;
		}
		current = current->next;
	}
	free(values);
	if (is_OK)
		return (1);
	else
		return (0);
}
