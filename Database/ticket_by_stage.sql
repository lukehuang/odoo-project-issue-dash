CREATE VIEW ticket_by_stage AS
SELECT project_issue.id,
       (SELECT task.name
FROM project_task_type task
WHERE (project_issue.stage_id = task.id)) AS stage
FROM project_issue
WHERE ((project_issue.state)::text <> ALL ((ARRAY['done'::character varying, 'cancelled'::character varying])::text[]))
