# Definition for singly-linked list node.
class ListNode:
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node


class Solution:
    def reverseKGroup(self, head_of_linked_list, group_size_k):
        """
        Reverse nodes in groups of k.

        Example:
        Input:
            1 -> 2 -> 3 -> 4 -> 5
            k = 2

        Output:
            2 -> 1 -> 4 -> 3 -> 5
        """

        # ------------------------------------------------------------
        # Edge case:
        # If the linked list is empty OR k is 1,
        # there is nothing to reverse.
        # ------------------------------------------------------------
        if head_of_linked_list is None or group_size_k == 1:
            return head_of_linked_list

        # ------------------------------------------------------------
        # Dummy node helps simplify pointer manipulation,
        # especially when the head changes after reversal.
        # ------------------------------------------------------------
        dummy_starting_node = ListNode(0)

        # Connect dummy node to the original head
        dummy_starting_node.next = head_of_linked_list

        # ------------------------------------------------------------
        # This pointer tracks the node BEFORE the current group.
        #
        # Example:
        # dummy -> 1 -> 2 -> 3 -> 4
        #          ^
        # group starts here
        #
        # Initially, previous_group_tail_node = dummy
        # ------------------------------------------------------------
        previous_group_tail_node = dummy_starting_node

        # ------------------------------------------------------------
        # Continue processing groups until we run out of nodes.
        # ------------------------------------------------------------
        while True:

            # --------------------------------------------------------
            # Step 1:
            # Check whether there are at least k nodes remaining.
            # --------------------------------------------------------
            kth_node_in_current_group = previous_group_tail_node

            for _ in range(group_size_k):

                # Move forward one node
                kth_node_in_current_group = kth_node_in_current_group.next

                # ----------------------------------------------------
                # If we hit None before reaching k nodes,
                # there are fewer than k nodes left.
                # Do NOT reverse them.
                # ----------------------------------------------------
                if kth_node_in_current_group is None:
                    return dummy_starting_node.next

            # --------------------------------------------------------
            # Step 2:
            # Identify important pointers.
            # --------------------------------------------------------

            # First node in current group
            current_group_head_node = previous_group_tail_node.next

            # Node AFTER the kth node
            next_group_head_node = kth_node_in_current_group.next

            # --------------------------------------------------------
            # Step 3:
            # Reverse the current group.
            #
            # Example before reversal:
            # 1 -> 2 -> 3 -> 4
            #
            # Example after reversal:
            # 4 -> 3 -> 2 -> 1
            # --------------------------------------------------------

            # Previous pointer starts at next group's head
            previous_node = next_group_head_node

            # Current pointer starts at group's head
            current_node = current_group_head_node

            # --------------------------------------------------------
            # Reverse exactly k nodes
            # --------------------------------------------------------
            for _ in range(group_size_k):

                # Save next node before changing pointers
                next_node_temporarily_saved = current_node.next

                # Reverse pointer direction
                current_node.next = previous_node

                # Move previous pointer forward
                previous_node = current_node

                # Move current pointer forward
                current_node = next_node_temporarily_saved

            # --------------------------------------------------------
            # Step 4:
            # Connect reversed group back into the list.
            # --------------------------------------------------------

            # After reversal:
            # previous_node is the NEW head of the reversed group
            previous_group_tail_node.next = previous_node

            # The old head becomes the tail after reversal
            previous_group_tail_node = current_group_head_node