--
-- TOC entry 202 (class 1259 OID 24783)
-- Name: account; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.account (
    account_number character varying(15) NOT NULL,
    branch_name character varying(15) NOT NULL,
    balance numeric NOT NULL
);


--
-- TOC entry 207 (class 1259 OID 24827)
-- Name: borrower; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.borrower (
    customer_name character varying(15) NOT NULL,
    loan_number character varying(15) NOT NULL
);


--
-- TOC entry 203 (class 1259 OID 24791)
-- Name: branch; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.branch (
    branch_name character varying(15) NOT NULL,
    branch_city character varying(15) NOT NULL,
    assets numeric NOT NULL
);


--
-- TOC entry 204 (class 1259 OID 24799)
-- Name: customer; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.customer (
    customer_name character varying(15) NOT NULL,
    customer_street character varying(12),
    customer_city character varying(15) NOT NULL
);


--
-- TOC entry 206 (class 1259 OID 24812)
-- Name: depositor; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.depositor (
    customer_name character varying(15) NOT NULL,
    account_number character varying(15) NOT NULL
);


--
-- TOC entry 205 (class 1259 OID 24804)
-- Name: loan; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.loan (
    loan_number character varying(15) NOT NULL,
    branch_name character varying(15) NOT NULL,
    amount numeric
);


--
-- TOC entry 2849 (class 0 OID 24783)
-- Dependencies: 202
-- Data for Name: account; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.account (account_number, branch_name, balance) VALUES ('A-101', 'Downtown', 500);
INSERT INTO public.account (account_number, branch_name, balance) VALUES ('A-215', 'Mianus', 700);
INSERT INTO public.account (account_number, branch_name, balance) VALUES ('A-102', 'Perryridge', 400);
INSERT INTO public.account (account_number, branch_name, balance) VALUES ('A-305', 'Round Hill', 350);
INSERT INTO public.account (account_number, branch_name, balance) VALUES ('A-201', 'Perryridge', 900);
INSERT INTO public.account (account_number, branch_name, balance) VALUES ('A-222', 'Redwood', 700);
INSERT INTO public.account (account_number, branch_name, balance) VALUES ('A-217', 'Brighton', 750);
INSERT INTO public.account (account_number, branch_name, balance) VALUES ('A-333', 'Central', 850);
INSERT INTO public.account (account_number, branch_name, balance) VALUES ('A-444', 'North Town', 625);
INSERT INTO public.account (account_number, branch_name, balance) VALUES ('A-666', 'West Coast', 1180);
INSERT INTO public.account (account_number, branch_name, balance) VALUES ('A-667', 'Downtown', 800);


--
-- TOC entry 2854 (class 0 OID 24827)
-- Dependencies: 207
-- Data for Name: borrower; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.borrower (customer_name, loan_number) VALUES ('Jones', 'L-17');
INSERT INTO public.borrower (customer_name, loan_number) VALUES ('Smith', 'L-23');
INSERT INTO public.borrower (customer_name, loan_number) VALUES ('Jackson', 'L-14');
INSERT INTO public.borrower (customer_name, loan_number) VALUES ('Curry', 'L-93');
INSERT INTO public.borrower (customer_name, loan_number) VALUES ('Smith', 'L-11');
INSERT INTO public.borrower (customer_name, loan_number) VALUES ('Williams', 'L-17');
INSERT INTO public.borrower (customer_name, loan_number) VALUES ('Adams', 'L-16');
INSERT INTO public.borrower (customer_name, loan_number) VALUES ('McBride', 'L-20');
INSERT INTO public.borrower (customer_name, loan_number) VALUES ('Smith', 'L-21');
INSERT INTO public.borrower (customer_name, loan_number) VALUES ('Hayes', 'L-155');
INSERT INTO public.borrower (customer_name, loan_number) VALUES ('Hayes', 'L-24');


--
-- TOC entry 2850 (class 0 OID 24791)
-- Dependencies: 203
-- Data for Name: branch; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.branch (branch_name, branch_city, assets) VALUES ('Downtown', 'Brooklyn', 900000);
INSERT INTO public.branch (branch_name, branch_city, assets) VALUES ('Redwood', 'Palo Alto', 2100000);
INSERT INTO public.branch (branch_name, branch_city, assets) VALUES ('Perryridge', 'Horseneck', 1700000);
INSERT INTO public.branch (branch_name, branch_city, assets) VALUES ('Mianus', 'Horseneck', 400200);
INSERT INTO public.branch (branch_name, branch_city, assets) VALUES ('Round Hill', 'Horseneck', 8000000);
INSERT INTO public.branch (branch_name, branch_city, assets) VALUES ('Pownal', 'Bennington', 400000);
INSERT INTO public.branch (branch_name, branch_city, assets) VALUES ('North Town', 'Rye', 3700000);
INSERT INTO public.branch (branch_name, branch_city, assets) VALUES ('Brighton', 'Brooklyn', 7000000);
INSERT INTO public.branch (branch_name, branch_city, assets) VALUES ('Central', 'Rye', 400280);


--
-- TOC entry 2851 (class 0 OID 24799)
-- Dependencies: 204
-- Data for Name: customer; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.customer (customer_name, customer_street, customer_city) VALUES ('Jones', 'Main', 'Harrison');
INSERT INTO public.customer (customer_name, customer_street, customer_city) VALUES ('Smith', 'Main', 'Rye');
INSERT INTO public.customer (customer_name, customer_street, customer_city) VALUES ('Hayes', 'Main', 'Harrison');
INSERT INTO public.customer (customer_name, customer_street, customer_city) VALUES ('Curry', 'North', 'Rye');
INSERT INTO public.customer (customer_name, customer_street, customer_city) VALUES ('Lindsay', 'Park', 'Pittsfield');
INSERT INTO public.customer (customer_name, customer_street, customer_city) VALUES ('Turner', 'Putnam', 'Stamford');
INSERT INTO public.customer (customer_name, customer_street, customer_city) VALUES ('Williams', 'Nassau', 'Princeton');
INSERT INTO public.customer (customer_name, customer_street, customer_city) VALUES ('Adams', 'Spring', 'Pittsfield');
INSERT INTO public.customer (customer_name, customer_street, customer_city) VALUES ('Johnson', 'Alma', 'Palo Alto');
INSERT INTO public.customer (customer_name, customer_street, customer_city) VALUES ('Glenn', 'Sand Hill', 'Woodside');
INSERT INTO public.customer (customer_name, customer_street, customer_city) VALUES ('Brooks', 'Senator', 'Brooklyn');
INSERT INTO public.customer (customer_name, customer_street, customer_city) VALUES ('Green', 'Walnut', 'Stamford');
INSERT INTO public.customer (customer_name, customer_street, customer_city) VALUES ('Jackson', 'University', 'Salt Lake');
INSERT INTO public.customer (customer_name, customer_street, customer_city) VALUES ('Majeris', 'First', 'Rye');
INSERT INTO public.customer (customer_name, customer_street, customer_city) VALUES ('McBride', 'Safety', 'Rye');
INSERT INTO public.customer (customer_name, customer_street, customer_city) VALUES ('Morty', NULL, 'Seattle');
INSERT INTO public.customer (customer_name, customer_street, customer_city) VALUES ('Lana del Rey', 'Bel Air Rd', 'Los Angeles');


--
-- TOC entry 2853 (class 0 OID 24812)
-- Dependencies: 206
-- Data for Name: depositor; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.depositor (customer_name, account_number) VALUES ('Johnson', 'A-101');
INSERT INTO public.depositor (customer_name, account_number) VALUES ('Smith', 'A-215');
INSERT INTO public.depositor (customer_name, account_number) VALUES ('Hayes', 'A-102');
INSERT INTO public.depositor (customer_name, account_number) VALUES ('Hayes', 'A-101');
INSERT INTO public.depositor (customer_name, account_number) VALUES ('Turner', 'A-305');
INSERT INTO public.depositor (customer_name, account_number) VALUES ('Johnson', 'A-201');
INSERT INTO public.depositor (customer_name, account_number) VALUES ('Jones', 'A-217');
INSERT INTO public.depositor (customer_name, account_number) VALUES ('Lindsay', 'A-222');
INSERT INTO public.depositor (customer_name, account_number) VALUES ('Majeris', 'A-333');
INSERT INTO public.depositor (customer_name, account_number) VALUES ('Smith', 'A-444');
INSERT INTO public.depositor (customer_name, account_number) VALUES ('Lana del Rey', 'A-666');
INSERT INTO public.depositor (customer_name, account_number) VALUES ('Lana del Rey', 'A-667');


--
-- TOC entry 2852 (class 0 OID 24804)
-- Dependencies: 205
-- Data for Name: loan; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.loan (loan_number, branch_name, amount) VALUES ('L-17', 'Downtown', 1000);
INSERT INTO public.loan (loan_number, branch_name, amount) VALUES ('L-23', 'Redwood', 2000);
INSERT INTO public.loan (loan_number, branch_name, amount) VALUES ('L-15', 'Perryridge', 1500);
INSERT INTO public.loan (loan_number, branch_name, amount) VALUES ('L-14', 'Downtown', 1500);
INSERT INTO public.loan (loan_number, branch_name, amount) VALUES ('L-93', 'Mianus', 500);
INSERT INTO public.loan (loan_number, branch_name, amount) VALUES ('L-11', 'Round Hill', 900);
INSERT INTO public.loan (loan_number, branch_name, amount) VALUES ('L-16', 'Perryridge', 1300);
INSERT INTO public.loan (loan_number, branch_name, amount) VALUES ('L-20', 'North Town', 7500);
INSERT INTO public.loan (loan_number, branch_name, amount) VALUES ('L-21', 'Central', 570);
INSERT INTO public.loan (loan_number, branch_name, amount) VALUES ('L-22', 'Midwest', NULL);
INSERT INTO public.loan (loan_number, branch_name, amount) VALUES ('L-24', 'Perryridge', 650);


--
-- TOC entry 2709 (class 2606 OID 24790)
-- Name: account account_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE public.account
    ADD CONSTRAINT account_pkey PRIMARY KEY (account_number);


--
-- TOC entry 2719 (class 2606 OID 24831)
-- Name: borrower borrower_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE public.borrower
    ADD CONSTRAINT borrower_pkey PRIMARY KEY (customer_name, loan_number);


--
-- TOC entry 2711 (class 2606 OID 24798)
-- Name: branch branch_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE public.branch
    ADD CONSTRAINT branch_pkey PRIMARY KEY (branch_name);


--
-- TOC entry 2713 (class 2606 OID 24803)
-- Name: customer customer_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE public.customer
    ADD CONSTRAINT customer_pkey PRIMARY KEY (customer_name);


--
-- TOC entry 2717 (class 2606 OID 24816)
-- Name: depositor depositor_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE public.depositor
    ADD CONSTRAINT depositor_pkey PRIMARY KEY (customer_name, account_number);


--
-- TOC entry 2715 (class 2606 OID 24811)
-- Name: loan loan_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE public.loan
    ADD CONSTRAINT loan_pkey PRIMARY KEY (loan_number);


--
-- TOC entry 2722 (class 2606 OID 24832)
-- Name: borrower borrower_customer_name_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE public.borrower
    ADD CONSTRAINT borrower_customer_name_fkey FOREIGN KEY (customer_name) REFERENCES public.customer(customer_name);


--
-- TOC entry 2720 (class 2606 OID 24817)
-- Name: depositor depositor_account_number_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE public.depositor
    ADD CONSTRAINT depositor_account_number_fkey FOREIGN KEY (account_number) REFERENCES public.account(account_number);


--
-- TOC entry 2721 (class 2606 OID 24822)
-- Name: depositor depositor_customer_name_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE public.depositor
    ADD CONSTRAINT depositor_customer_name_fkey FOREIGN KEY (customer_name) REFERENCES public.customer(customer_name);


-- Completed on 2020-09-18 12:46:10

--
-- PostgreSQL database dump complete
--

