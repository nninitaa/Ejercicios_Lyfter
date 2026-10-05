ALTER TABLE "Bills"
ADD COLUMN status VARCHAR(30) DEFAULT 'Pending';

DROP TABLE IF EXISTS Shopping;

CREATE TEMP TABLE Shopping (
    id_product INTEGER,
    quantity INTEGER
);

INSERT INTO Shopping (id_product, quantity)
VALUES
    (1, 2),
    (2, 3);

BEGIN;

DO $$
BEGIN
    IF EXISTS (
        SELECT 1
        FROM Shopping s
        JOIN "Products" p
            ON p.id_product = s.id_product
        WHERE p.stock < s.quantity
    ) THEN
        RAISE EXCEPTION 'Not enough stock';
    END IF;
END $$;

DO $$
BEGIN
    IF NOT EXISTS (
        SELECT 1
        FROM "Users"
        WHERE id_user = 1
    ) THEN
        RAISE EXCEPTION 'User does not exist';
    END IF;
END $$;


INSERT INTO "Bills" (
    id_user,
    bill_date,
    total
)
VALUES (
    1,
    CURRENT_DATE,
    (
        SELECT SUM(p.price * s.quantity)
        FROM Shopping s
        JOIN "Products" p
            ON p.id_product = s.id_product
    )
);

INSERT INTO "Bill_Products" (
    id_bill,
    id_product,
    quantity,
    unit_price
)
SELECT
    (SELECT MAX(id_bill) FROM "Bills"),
    s.id_product,
    s.quantity,
    p.price
FROM Shopping s
JOIN "Products" p
    ON p.id_product = s.id_product;

UPDATE "Products" p
SET stock = p.stock - s.quantity
FROM Shopping s
WHERE p.id_product = s.id_product;

COMMIT;

BEGIN;

DO $$
BEGIN
    IF NOT EXISTS (
        SELECT 1
        FROM "Bills"
        WHERE id_bill = 1
    ) THEN
        RAISE EXCEPTION 'Invoice does not exist';
    END IF;
END $$;

DO $$
BEGIN
    IF EXISTS (
        SELECT 1
        FROM "Bills"
        WHERE id_bill = 1
        AND status = 'Retornada'
    ) THEN
        RAISE EXCEPTION 'Invoice already returned';
    END IF;
END $$;

UPDATE "Products" p
SET stock = p.stock + bp.quantity
FROM "Bill_Products" bp
WHERE p.id_product = bp.id_product
AND bp.id_bill = 1;

UPDATE "Bills"
SET status = 'Retornada'
WHERE id_bill = 1;

COMMIT;

