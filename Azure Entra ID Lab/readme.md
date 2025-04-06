# 🔐 Azure Entra ID Lab – User, Group, and Role Management

This lab demonstrates how to create and manage users in Azure Entra ID, assign roles and groups, and configure authentication settings — all using the example of a user named **Alex Intern**. This setup reflects real-world identity and access management tasks aligned with NIST and CIS security practices.

---

## 📋 Objectives

- ✅ Create a new internal user (Alex Intern)  
- ✅ Assign security groups  
- ✅ Grant administrative roles  
- ✅ Configure MFA and conditional access settings  
- ✅ Disable security defaults to simulate legacy auth scenarios

---

## 👨‍💻 Steps Performed

### 1️⃣ Create User: **Alex Intern**
- Navigated to **Microsoft Entra ID > Users > + New user**
- Filled in:
  - Display name: `Alex Intern`
  - User name: `intern@<domain>.onmicrosoft.com`
  - Auto-generated temporary password
- Created the user with **Member** type

📸 _Screenshot: New user added to group_
![New user](./new%20user%20added%20to%20group.png)

---

### 2️⃣ Assign User to Security Group (Optional)
- Navigated to **Groups > + New group**
- Created a new **Security** group named `Interns`
- Added **Alex Intern** to the group under **Group memberships**

📸 _Screenshot: Create security group_
![Security group](./Create%20security%20group.png)

---

### 3️⃣ Assign Roles to User
- From **Users > Alex Intern > Assigned Roles**
- Assigned **Attribute Assignment Reader** to provide minimal read access
- Additional roles (e.g., Helpdesk Administrator, Intune roles) can be added based on policy needs

📸 _Screenshot: Assigned role to Alex_
![Role assignment](./Assigned%20role%20to%20ALex.png)

---

## ⚙️ User Settings Overview
From **Microsoft Entra ID > User settings**:
- Users can register apps: ✅ Yes
- Users can create security groups: ✅ Yes
- Guest users have default member-like access: 🔄 Adjustable

---

## 📌 Learning Outcomes

- 🔐 Understood how to manage identity lifecycles in Azure
- 🛡 Practiced secure role assignment and least privilege principles
- 🚫 Simulated legacy auth environments by disabling defaults
- ⚠️ Explored MFA controls and user-specific auth policies

---

> 💡 This lab is for demonstrating role-based access control (RBAC), compliance-driven identity design, and foundational IAM operations in a cloud enterprise setting.

