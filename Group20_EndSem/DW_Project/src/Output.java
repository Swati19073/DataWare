//package dw;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;



public class Output {
	private Connection conn;
	private String db_name;
	private ArrayList<String> facts;
	private HashMap<String,ArrayList<String>> dimensions;
	private HashMap<String,HashMap<String,ArrayList<String>>> subdimensions;
	
	public Output(String pid)
	{
		DatabaseConnection dbcon=new DatabaseConnection();
		this.db_name=pid;
		this.conn=dbcon.getConnection(pid);
		
	}
	public void getFacts() 
	{
		facts=new ArrayList<String>();
		Statement stmt;
		try {
			stmt = conn.createStatement();
			String sql="USE "+db_name;
			stmt.executeUpdate(sql);
			ResultSet rs=null;
			sql = "Select p_info from p_info";
			if (stmt.execute(sql )) {
				rs = stmt.getResultSet();
	                      }
			
			if(rs!=null)
			{
				while(rs.next())
				{
					facts.add(rs.getString(1));
				}
			}
			
		} catch (SQLException e1) {
			// TODO Auto-generated catch block
			e1.printStackTrace();
		}

}
	
	public void getDimensions()
	{
		dimensions=new HashMap<String,ArrayList<String>>();
		ArrayList<String> temp=new ArrayList<String>();
		Statement stmt;
		try {
			stmt = conn.createStatement();
			String sql="USE "+db_name;
			stmt.executeUpdate(sql);
			ResultSet rs=null;
			sql = "Select p_info,category_name from category_subcategory where subcategory_of IS NULL";
			if (stmt.execute(sql )) {
				rs = stmt.getResultSet();
	                      }
//			
//			if(rs!=null)
//			{
//				while(rs.next())
//				{
//					String f=rs.getString(1);
//					dimensions.put(f, temp);
//					
//				}
//			}
			if(rs!=null)
			{
				while(rs.next())
				{
					String f=rs.getString(1);
					ArrayList<String> reqArrayList;
					String d=rs.getString(2);
					if(dimensions.get(f)!=null)
					{
						reqArrayList=dimensions.get(f);
					}
					else
					{
						reqArrayList=new ArrayList<String>();
					}
					reqArrayList.add(d);
					dimensions.put(f,reqArrayList);
					
					
				}
			}
		} catch (SQLException e1) {
			// TODO Auto-generated catch block
			e1.printStackTrace();
		}
	}
	public void getSubdimensions()
	{
		subdimensions=new HashMap<String,HashMap<String,ArrayList<String>>>();
		HashMap<String,ArrayList<String>> temp=new HashMap<String,ArrayList<String>>();
		
		Statement stmt;
		try {
			stmt = conn.createStatement();
			String sql="USE "+db_name;
			stmt.executeUpdate(sql);
			ResultSet rs=null;
			sql = "Select p_info,subcategory_of,category_name from category_subcategory";
			if (stmt.execute(sql )) {
				rs = stmt.getResultSet();
	                      }
			
//			if(rs!=null)
//			{
//				while(rs.next())
//				{
//					String f=rs.getString(1);
//					
//					subdimensions.put(f,temp);
//					
//					
//
//				}
//			}
			if(rs!=null)
			{
				while(rs.next())
				{
					String f=rs.getString(1);
					HashMap <String,ArrayList<String>> inner;
					if(subdimensions.get(f)!=null)
					{
						inner=subdimensions.get(f);
					}
					else
					{
						inner=new HashMap<String,ArrayList<String>>();
					}
					String d=rs.getString(2);
					String sd=rs.getString(3);
					if(inner.get(d)!=null)
					{
					inner.get(d).add(sd);
					subdimensions.put(f,inner);
					}
					else
					{
						ArrayList<String> temp2=new ArrayList<String>();
						temp2.add(sd);
						inner.put(d,temp2);
						subdimensions.put(f, inner);
						
					}
					
					

				}
			}
			
		} catch (SQLException e1) {
			// TODO Auto-generated catch block
			e1.printStackTrace();
		}
	}
	
	public void printOutput()
	{
		getFacts();
		getDimensions();
		getSubdimensions();
		for(String f:facts)
		{
			System.out.println("Fact:");
//			System.out.println(f);
			
			String f_schema=f+" (";
			Statement stmt;
			try {
				stmt = conn.createStatement();
				String sql="USE "+db_name;
				stmt.executeUpdate(sql);
				
				String query_countf = "Select COUNT(COLUMN_NAME) from INFORMATION_SCHEMA.COLUMNS where TABLE_NAME= (?) and COLUMN_NAME NOT like '%primary_key%' AND COLUMN_NAME NOT like '%foreign_key%'";
				PreparedStatement pst_countf = conn.prepareStatement(query_countf);
				pst_countf.setString(1,f);
				ResultSet rs_countf=pst_countf.executeQuery();
				int n=-1;
				if(rs_countf!=null)
				{
					while(rs_countf.next())
					{
				n=rs_countf.getInt(1);
				
					}}
				int count_f=1;
				
				
				
				String query_schemaf = "Select COLUMN_NAME from INFORMATION_SCHEMA.COLUMNS where TABLE_NAME= (?) and COLUMN_NAME NOT like '%primary_key%' AND COLUMN_NAME NOT like '%foreign_key%' ";
				PreparedStatement pst3f = conn.prepareStatement(query_schemaf);
				pst3f.setString(1,f);
				ResultSet rs_f=pst3f.executeQuery();
				
				if(rs_f!=null)
				{
					while(rs_f.next())
					{
						if(count_f<n)
						{
							f_schema=f_schema+rs_f.getString(1)+",";
						}
						else
						{
							f_schema=f_schema+rs_f.getString(1)+")";
						}
						count_f++;
						
					}
				}
				System.out.println(f_schema);
				
			} catch (SQLException e1) {
				// TODO Auto-generated catch block
				e1.printStackTrace();
			}
			ArrayList<String> dims=dimensions.get(f);
			
			HashMap<String,ArrayList<String>> subdims_map=subdimensions.get(f);
			for(String d:dims)
			{
				
				System.out.println("Dimensions:");
//				System.out.println(d);
				String d_schema=d+" (";
				
				try {
					stmt = conn.createStatement();
					String sql="USE "+db_name;
					stmt.executeUpdate(sql);
					
					String query_count = "Select COUNT(COLUMN_NAME) from INFORMATION_SCHEMA.COLUMNS where TABLE_NAME= (?) and COLUMN_NAME NOT like '%primary_key%' AND COLUMN_NAME NOT like '%foreign_key%' ";
					PreparedStatement pst_count = conn.prepareStatement(query_count);
					pst_count.setString(1,d);
					ResultSet rs_count=pst_count.executeQuery();
					int n_d=-1;
					if(rs_count!=null)
					{
						while(rs_count.next())
						{
					n_d=rs_count.getInt(1);
					
						}}
					int count_d=1;
					
					
					
					String query_schema = "Select COLUMN_NAME from INFORMATION_SCHEMA.COLUMNS where TABLE_NAME= (?) and COLUMN_NAME NOT like '%primary_key%' AND COLUMN_NAME NOT like '%foreign_key%'";
					PreparedStatement pst3=conn.prepareStatement(query_schema);
					pst3.setString(1,d);
					ResultSet rs_dim=pst3.executeQuery();
					
					if(rs_dim!=null)
					{
						while(rs_dim.next())
						{
							if(count_d<n_d)
							{
								d_schema=d_schema+rs_dim.getString(1)+",";
							}
							else
							{
								d_schema=d_schema+rs_dim.getString(1)+")";
							}
							count_d++;
							
						}
					}
					System.out.println(d_schema);
					
				} catch (SQLException e1) {
					// TODO Auto-generated catch block
					e1.printStackTrace();
				}
				if(subdimensions.containsKey(f))
				{
				if(subdims_map.containsKey(d))
				{
				ArrayList<String> reqSubdims=subdims_map.get(d);
				
				for(String sd: reqSubdims)
				{
					System.out.println("Subdimensions:");
//					System.out.println(sd);
					String sd_schema=sd+" (";
					
					try {
						stmt = conn.createStatement();
						String sql="USE "+db_name;
						stmt.executeUpdate(sql);
						
						String query_countsd = "Select COUNT(COLUMN_NAME) from INFORMATION_SCHEMA.COLUMNS where TABLE_NAME= (?) and COLUMN_NAME NOT like '%primary_key%' AND COLUMN_NAME NOT like '%foreign_key%'";
						PreparedStatement pst_countsd = conn.prepareStatement(query_countsd);
						pst_countsd.setString(1,sd);
						ResultSet rs_countsd=pst_countsd.executeQuery();
						int n_sd=-1;
						if(rs_countsd!=null)
						{
							while(rs_countsd.next())
							{
						n_sd=rs_countsd.getInt(1);
						
						
							}}
						int count_sd=1;
						
						
						
						String query_schemasd = "Select COLUMN_NAME from INFORMATION_SCHEMA.COLUMNS where TABLE_NAME= (?) and COLUMN_NAME NOT like '%primary_key%' AND  COLUMN_NAME NOT like '%foreign_key%'";
						PreparedStatement pst3sd = conn.prepareStatement(query_schemasd);
						pst3sd.setString(1,sd);
						ResultSet rs_sd=pst3sd.executeQuery();
						
						if(rs_sd!=null)
						{
							while(rs_sd.next())
							{
								if(count_sd<n_sd)
								{
									sd_schema=sd_schema+rs_sd.getString(1)+",";
								}
								else
								{
									
									sd_schema=sd_schema+rs_sd.getString(1)+")";
								}
								count_sd++;
								
							}
						}
						System.out.println(sd_schema);
						
					} catch (SQLException e1) {
						// TODO Auto-generated catch block
						e1.printStackTrace();
					}
				}
				}
				}
				
				
				
			}
			
			
		}
	}
	
}
