#include "lists.h"
/**
 * palindrome - check for palindrome
 * @l: l
 * @r: r
 *
 * Return: 1 palindrome, 0 not palindrome
 */
int palindrome(listint_t **l, listint_t *r)
{
	int res;

	if (r != NULL)
	{
		res = palindrome(l, r->next);
		if (res != 0)
		{
			res = (r->n == (*l)->n);
			*l = (*l)->next;
			return (res);
		}
		return (0);
	}
	return (1);
}
/**
 * is_palindrome - checks if list is a palindrome
 * @head: head of linked_list
 *
 * Return: 1 palindrome, 0 mot palindrome
 */

int is_palindrome(listint_t **head)
{
	if (head == NULL)
	{
		return (0);
	}
	return (palindrome(head, *head));
}
