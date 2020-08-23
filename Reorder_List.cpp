/* Reorder List 문제

Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:
Given 1->2->3->4, reorder it to 1->4->2->3.

Example 2:
Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
*/

/* 나의 문제 풀이

처음엔 Python으로 풀려했으나, Python에는 Linked List를 지원해주는 함수가 없으며 주소 접근에도 불편하다.
따라서 C++이라는 언어로 변경하여 Pointer를 사용하여 풀었다.
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

        int count = 0; // 노드 개수
        ListNode* pointer = head;
        ListNode* use_pointer = head;
        ListNode* temp;
        ListNode* node_temp; // 사용한 노드 없애기위한 포인터

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
            node_temp->next = nullptr; // 마지막 노드 연결 해제   
            use_pointer = use_pointer->next->next;

            pointer = head;
        }
    }
};