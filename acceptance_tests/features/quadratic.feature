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
