CREATE VIEW calls_by_status AS
SELECT project_issue.stage_id AS
 id, count(project_issue.stage_id) AS nooftickets,
 (SELECT task.name FROM project_task_type task WHERE (project_issue.stage_id = task.id)) AS stage
FROM project_issue
WHERE ((project_issue.state)::text <> ALL ((ARRAY['done'::character varying, 'cancelled'::character varying])::text[])) 
GROUP BY project_issue.stage_id;
