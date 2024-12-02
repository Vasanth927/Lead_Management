import React, { useEffect, useState } from "react";
import axios from "axios";

const LeadManagement = () => {
  const [leads, setLeads] = useState([]);
  const [newLead, setNewLead] = useState({ name: "", contact_info: "", platform: "" });

  useEffect(() => {
    fetchLeads();
  }, []);

  const fetchLeads = async () => {
    const response = await axios.get("http://127.0.0.1:5000/leads");
    setLeads(response.data);
  };

  const addLead = async () => {
    await axios.post("http://127.0.0.1:5000/leads", newLead);
    fetchLeads();
    setNewLead({ name: "", contact_info: "", platform: "" });
  };

  const deleteLead = async (id) => {
    await axios.delete(`http://127.0.0.1:5000/leads/${id}`);
    fetchLeads();
  };

  return (
    <div>
      <h1>Lead Management</h1>
      <div>
        <input
          type="text"
          placeholder="Name"
          value={newLead.name}
          onChange={(e) => setNewLead({ ...newLead, name: e.target.value })}
        />
        <input
          type="text"
          placeholder="Contact Info"
          value={newLead.contact_info}
          onChange={(e) => setNewLead({ ...newLead, contact_info: e.target.value })}
        />
        <input
          type="text"
          placeholder="Platform"
          value={newLead.platform}
          onChange={(e) => setNewLead({ ...newLead, platform: e.target.value })}
        />
        <button onClick={addLead}>Add Lead</button>
      </div>
      <ul>
        {leads.map((lead) => (
          <li key={lead.id}>
            {lead.name} - {lead.status}
            <button onClick={() => deleteLead(lead.id)}>Delete</button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default LeadManagement;
