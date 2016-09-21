# Created by askar at 9/20/16
Feature: test for quadratic
  # Enter feature description here

  Scenario: i should not possible text
    Given i open "quadratic" page
    And i enter into "a" field a "5"
    And i enter into "b" field a "2"
    And i enter into "c" field a "1"
    When click button submit
    Then i see "Решений нет!!!" text

  Scenario: i should see 1 answer
    Given i open "quadratic" page
    And i enter into "a" field a "1"
    And i enter into "b" field a "-4"
    And i enter into "c" field a "4"
    When click button submit
    Then i see 1 answer "2" text

  Scenario: i should see 2 answer
    Given i open "quadratic" page
    And i enter into "a" field a "5"
    And i enter into "b" field a "6"
    And i enter into "c" field a "1"
    When click button submit
    Then i see 2 answer "-0.2" and "-1" text

  Scenario: i should see 2.1 answer
    Given i open "quadratic" page
    And i enter into "a" field a "1"
    And i enter into "b" field a "2"
    And i enter into "c" field a "-8"
    When click button submit
    Then i see 2 answer "2" and "-4" text

  Scenario: i should see 2.21 answer
    Given i open "quadratic" page
    And i enter into "a" field a "1"
    And i enter into "b" field a "-7"
    And i enter into "c" field a "0"
    When click button submit
    Then i see 2 answer "7" and "0" text

  Scenario: i try enter character
    Given i open "quadratic" page
    And i enter into "a" field a "qwe"
    And i enter into "b" field a "asd"
    And i enter into "c" field a "zxc"
    When click button submit
    Then i see "Please enter a valid number." error message in "a" field
    And i see "Please enter a valid number." error message in "b" field
    And i see "Please enter a valid number." error message in "c" field

  Scenario: i try enter greater more 100000
    Given i open "quadratic" page
    And i enter into "a" field a "100001"
    And i enter into "b" field a "100002"
    And i enter into "c" field a "100003"
    When click button submit
    Then i see "Please enter a value between -100000 and 100000." error message in "a" field
    And i see "Please enter a value between -100000 and 100000." error message in "b" field
    And i see "Please enter a value between -100000 and 100000." error message in "c" field

  Scenario: i try enter greater less -100000
    Given i open "quadratic" page
    And i enter into "a" field a "-100001"
    And i enter into "b" field a "-100002"
    And i enter into "c" field a "-100003"
    When click button submit
    Then i see "Please enter a value between -100000 and 100000." error message in "a" field
    And i see "Please enter a value between -100000 and 100000." error message in "b" field
    And i see "Please enter a value between -100000 and 100000." error message in "c" field

  Scenario: i try type number with 2 point
    Given i open "quadratic" page
    And i enter into "a" field a "100..2"
    And i enter into "b" field a "1.0.2"
    And i enter into "c" field a "100.."
    When click button submit
    Then i see "Please enter a valid number." error message in "a" field
    And i see "Please enter a valid number." error message in "b" field
    And i see "Please enter a valid number." error message in "c" field

  Scenario: i try type number with 2 dash
    Given i open "quadratic" page
    And i enter into "a" field a "--1002"
    And i enter into "b" field a "1-0-2"
    And i enter into "c" field a "100-"
    When click button submit
    Then i see "Please enter a valid number." error message in "a" field
    And i see "Please enter a valid number." error message in "b" field
    And i see "Please enter a valid number." error message in "c" field
