# remove the first occurrence
  def remove_node(self, value_to_remove):
    current_node = self.head_node
    if current_node.value == value_to_remove:
      self.head_node = current_node.next_node
    else:
      while current_node:
        current_next_node = current_node.next_node
        if current_next_node.value == value_to_remove:
          current_node.next_node = current_next_node.next_node
          current_node = None
        else:
          current_node = current_next_node
          
          
          
          
# remove all occurrences
  def remove_node(self, value_to_remove):
    current_node = self.head_node
    if current_node.value == value_to_remove:
      self.head_node = current_node.next_node
    else:
      while current_node.next_node:
        current_next_node = current_node.next_node
        if current_next_node.value == value_to_remove:
          current_node.next_node = current_next_node.next_node
          current_next_node = None
        else:
          current_node = current_next_node
