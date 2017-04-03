CREATE VIEW inprogress_by_user AS
  SELECT project_issue.id,
  (SELECT res_users.login FROM res_users WHERE (res_users.id = project_issue.user_id)) AS "user",
  project_issue.user_id
FROM project_issue
WHERE (project_issue.stage_id = 33);
