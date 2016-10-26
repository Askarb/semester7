# Created by askar at 10/14/16
Feature: #Enter feature name here
  # Enter feature description here

  @vip
  Scenario: i try enter 1
    Given i open fibonacci page
    And i enter into "a" field a "1"
    When click button submit
      Then i see "1" number
  @vip
  Scenario: i try enter 2
    Given i open fibonacci page
    And i enter into "a" field a "2"
    When click button submit
      Then i see "1" number
  @vip
  Scenario: i try enter 3
    Given i open fibonacci page
    And i enter into "a" field a "3"
    When click button submit
      Then i see "2" number
  @vip
  Scenario: i try enter 4
    Given i open fibonacci page
    And i enter into "a" field a "4"
    When click button submit
      Then i see "3" number
  @vip
  Scenario: i try enter 5
    Given i open fibonacci page
    And i enter into "a" field a "5"
    When click button submit
      Then i see "5" number
  @vip
  Scenario: i try enter 6
    Given i open fibonacci page
    And i enter into "a" field a "6"
    When click button submit
      Then i see "8" number
  @vip
  Scenario: i try enter 10
    Given i open fibonacci page
    And i enter into "a" field a "10"
    When click button submit
      Then i see "55" number
  @vip
  Scenario: i try enter 20
    Given i open fibonacci page
    And i enter into "a" field a "20"
    When click button submit
      Then i see "6765" number
  @vip
  Scenario: i try enter 50
    Given i open fibonacci page
    And i enter into "a" field a "50"
    When click button submit
      Then i see "12586269025" number
  @vip
  Scenario: i try enter 100
    Given i open fibonacci page
    And i enter into "a" field a "100"
    When click button submit
      Then i see "354224848179261915075" number
  @vip
  Scenario: i try enter 4
    Given i open fibonacci page
    And i enter into "a" field a "200"
    When click button submit
      Then i see "280571172992510140037611932413038677189525" number