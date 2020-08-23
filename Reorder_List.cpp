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