SELECT DISTINCT DATE(lessons.scheduled_time) AS `day`,
     FIRST_VALUE(users.id) OVER (PARTITION BY lessons.scheduled_time) AS tutor_id,
       FIRST_VALUE(tbl.aver) OVER (PARTITION BY lessons.scheduled_time) AS average_score
  FROM users
JOIN participants
     ON participants.user_id = users.id
JOIN lessons
       ON lessons.event_id = participants.event_id
      AND lessons.subject = 'phys'
     JOIN ( SELECT users.id, AVG(quality.tech_quality) AS aver
          FROM users
    JOIN participants
         ON participants.user_id = users.id
    JOIN lessons
           ON lessons.event_id = participants.event_id
           AND lessons.subject = 'phys'
    JOIN quality
            ON quality.lesson_id = lessons.id
         WHERE users.role = 'tutor'
        GROUP BY users.id, lessons.scheduled_time
        ORDER BY aver ASC) AS tbl
    WHERE users.role = 'tutor'
    ORDER BY average_score LIMIT 1;