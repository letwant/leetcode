 ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* front = head;
        ListNode* behind = head;
        for (int i = 0; i < n - 2; i++)
        {
            behind = behind->next;
        }
        while (behind->next != NULL)
        {
            front = front->next;
            behind = behind->next;
        }
        ListNode* tmp = front->next;
        front->next = tmp->next;
        free(tmp);
        return head;
    }