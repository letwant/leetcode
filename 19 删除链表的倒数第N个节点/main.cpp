struct ListNode
{
	int val;
	ListNode *next;
	ListNode(int x) : val(x), next(NULL) {}
};
ListNode* CreateLinkList(int n) {
	ListNode *p, *r, *list;
	p = nullptr;
	r = nullptr;
	list = nullptr;
	int e;
	int i;
	for (i = 1; i <= n; i++) {
		cin >> e;
		p = (ListNode*)malloc(sizeof(ListNode));
		p->val = e;
		p->next = NULL;
		if (!list)
			list = p;
		else
			r->next = p;
		r = p;
	}
	return list;
}
ListNode* removeNthFromEnd(ListNode* head, int n) {
	// 使用new方法替代ListNode *p = (ListNode*)malloc(sizeof(ListNode))，
	// 因为ListNode有构造函数，所以直接new就行了
	// 使用头结点方便操作链表只有一个结点时的情况
	ListNode *p = new ListNode(0);
	p->next = head;
	ListNode* front = p;
	ListNode* behind = p;
	// 为什么是n+1？因为如果是n的话，front和behind就是相连的，不好进行删除操作
	// 假设n是1，则behind = front->next->next，只要删除behind->next即可
	for (int i = 0; i < n + 1; i++)
	{
		behind = behind->next;
	}
	// 不能使用behind->next!=NULL这种判断
	while (behind)
	{
		front = front->next;
		behind = behind->next;
	}
	cout << "behind =" << front->next->val << endl;
	ListNode* tmp = front->next;
	front->next = tmp->next;
	tmp->next = nullptr;
	delete tmp;
	ListNode* retNode = p->next;
	p->next = nullptr;
	delete p;
	return retNode;
}
int main()
{
	ListNode* phead = CreateLinkList(5);
	ListNode* pNode = phead;
	cout << "pNode =" << pNode->val << endl;
	while (pNode->next != nullptr)
	{
		pNode = pNode->next;
		cout << "pNode =" << pNode->val << endl;
	}
	ListNode* pVal = removeNthFromEnd(phead, 1);
	cout << "pVal =" << pVal->val << endl;
	while (pVal->next != nullptr)
	{
		pVal = pVal->next;
		cout << "pVal =" << pVal->val << endl;
	}
	system("pause");
	return 0;
}