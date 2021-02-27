# changeinsharescsv
-   to install before running:
    -   when installing python, be sure that you check the checkbox that says "environment variable" because python needs to be in your system path
    -   pip install pandas
    -   pip install openpyxl
-   run from directory:
    -   curl -o arkg_holdings.csv https://ark-funds.com/wp-content/fundsiteliterature/csv/ARK_GENOMIC_REVOLUTION_MULTISECTOR_ETF_ARKG_HOLDINGS.csv
    -   python update_shares.py
hw1
    R-2.11
        Read it.
        Ship it.
        Buy it.
        Read it.
        Box it.
        Read it.
    Given an array of size n >= 2 containing integers from 1 to n-1 inclusive, one of which is repeated.
        Describe an O(n^2 ) algorithm for finding the integer in the array that is repeated.
            Use a nested for loop
            
        Describe an O(n) algorithm to do the same.
            
    Given a singly linked list and a value, how do you remove the first node in the list that contains the given value?
        O(n)
        The first while loop iterates from the head to find the node containing the given value, and the second while loop iterates from the head to find the node that is before the node containing the given value and set the pointer of that node to the node after the node containing the given value.
        Node cursor = head;
Node removed = null; 
boolean found = false;
while (cursor.getNext() != null && !found){
	if (cursor.getElement() == value){
		removed = cursor;
		found = true;
	}
	cursor = cursor.getNext();	
}
cursor = head;
found = false;
while (cursor.getNext() != null && !found) {
	if (cursor.getNext() == removed){
		cursor.setNext(removed.getNext());
		found = true;
	}
	cursor = cursor.getNext();
}
        better: pointer and trailing pointer
        from javacompiler
            Node pointer = n1; 
        Node cursor = n1;
        Node removed = null;
        boolean found = false;
        while (cursor.getNext() != null && !found){
        	if (cursor.getElement() == value){
        	    removed = cursor;
        		found = true;
        	}
        	cursor = cursor.getNext();	
        }
        cursor = n1;
        found = false;
        while (cursor.getNext() != null && !found) {
        	if (cursor.getNext() == removed){
        		cursor.setNext(removed.getNext());
        		found = true;
        	}
        	cursor = cursor.getNext();
        }
         while (pointer != null){
            System.out.print(pointer.val);
            pointer = pointer.next;
        }
     }
        doubly!!!
            Node cursor = head;
boolean found = false;
while (cursor.getNext() != null && !found){
	if (cursor.getElement() == value){
		Node predecessor = cursor.getPrev();
		Node successor = cursor.getNext();
		predecessor.setNext(successor);
		successor.setPrev(predecessor);
		found = true;	
	}
	cursor = cursor.getNext;
}
