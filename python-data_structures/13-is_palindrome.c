#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: double pointer to the head of the list
 *
 * Return: 1 if it is a palindrome, 0 if it is not
 */
int is_palindrome(listint_t **head)
{
	listint_t *current;
	int *arr;
	int i, n = 0;

	if (head == NULL || *head == NULL || (*head)->next == NULL)
		return (1);

	current = *head;
	while (current != NULL)
	{
		n++;
		current = current->next;
	}

	arr = malloc(sizeof(int) * n);
	if (arr == NULL)
		return (0);

	current = *head;
	for (i = 0; i < n; i++)
	{
		arr[i] = current->n;
		current = current->next;
	}

	for (i = 0; i < n / 2; i++)
	{
		if (arr[i] != arr[n - 1 - i])
		{
			free(arr);
			return (0);
		}
	}

	free(arr);
	return (1);
}
