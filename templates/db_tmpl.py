{%- for i in identifiers -%} 
resource "aws_db_instance" "{{ i.identifier }}" {
  {% for key, value in i.items() %}
   {% if key != 'team' %}
  {{ key }} = "{{ value }}"
   {%endif %}
  {% endfor %}
}

output "{{ i.identifier }}-endpoint" {
  value = "${aws_db_instance.{{ i.identifier }}.endpoint}"
}

resource "aws_sns_topic" "{{ i.identifier }}-rds" {
  name = "{{ i.identifier }}-rds"
}

resource "aws_cloudwatch_metric_alarm" "{{ i.identifier }}_rds_full_alarm" {
  alarm_name          = "{{ i.identifier }}-rds-free-space-less-than-20_percent"
  metric_name         = "FreeStorageSpace"
  namespace           = "AWS/RDS"
  evaluation_periods  = "1"
  period              = "60"
  comparison_operator = "LessThanThreshold"
  statistic           = "Average"
  threshold           = "2147483648"

  dimensions {
    "DBInstanceIdentifier" = "${aws_db_instance.{{ i.identifier }}.id}"
  }

  alarm_description         = "The database has less than 20% of free space left."
  alarm_actions             = ["${aws_sns_topic.{{ i.identifier }}-rds.arn}"]
  insufficient_data_actions = ["${aws_sns_topic.{{ i.identifier }}-rds.arn}"]
  ok_actions                = ["${aws_sns_topic.{{ i.identifier }}-rds.arn}"]
}

{% endfor %}
