-- Script that creates a trigger that decreases the quantity of an item after adding a new order.
-- Quantity in the table items can be negative.

DELIMITER //
CREATE TRIGGER quantity_decrease
AFTER INSERT ON order 
FOR EACH ROW
BEGIN
    UPDATE items
    SET quantity = (new.number - quantity)
    WHERE name = NEW.item_name;
END;
//

DELIMITER ;
