/* Reorder List ����

Given a singly linked list L: L0��L1�桦��Ln-1��Ln,
reorder it to: L0��Ln��L1��Ln-1��L2��Ln-2�桦

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:
Given 1->2->3->4, reorder it to 1->4->2->3.

Example 2:
Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
*/

/* ���� ���� Ǯ��

ó���� Python���� Ǯ��������, Python���� Linked List�� �������ִ� �Լ��� ������ �ּ� ���ٿ��� �����ϴ�.
���� C++�̶�� ���� �����Ͽ� Pointer�� ����Ͽ� Ǯ����.
*/

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    void reorderList(ListNode* head) {

        int count = 0; // ��� ����
        ListNode* pointer = head;
        ListNode* use_pointer = head;
        ListNode* temp;
        ListNode* node_temp; // ����� ��� ���ֱ����� ������

        while (pointer) {
            pointer = pointer->next;
            count++;
        }
        pointer = head;

        for (int j = 1; j <= (count - 1) / 2; j++) {
            for (int i = 0; i < count - 1; ++i) {
                if (i == count - 2) {
                    node_temp = pointer;
                }
                pointer = pointer->next;
            }

            temp = use_pointer->next;
            use_pointer->next = pointer;
            use_pointer->next->next = temp; // head->next = temp
            node_temp->next = nullptr; // ������ ��� ���� ����   
            use_pointer = use_pointer->next->next;

            pointer = head;
        }
    }
};