//package dw;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.SQLIntegrityConstraintViolationException;
import java.sql.Statement;
import java.util.ArrayList;

public class endSemQueries {
	
	private Connection conn;
	private String db_name;
	public endSemQueries(String pid)
	{
	DatabaseConnection dbcon=new DatabaseConnection();
		this.db_name=pid;
		this.conn=dbcon.getConnection(pid);
		
	}
	public boolean createTables()
	{
		boolean success=true;
		System.out.println("CREATING TABLES FOR FACTS");
		
		String sql = null;
		ResultSet rs=null;
		try {
			Statement stmt = conn.createStatement();

						sql="USE "+db_name;
						stmt.executeUpdate(sql);

						sql = "Select p_info from p_info";
						if (stmt.execute(sql )) {
							rs = stmt.getResultSet();
			                                
						}
						if(rs!=null)
						{
							while (rs.next()) {
								String result=rs.getString(1);
			                                   
								System.out.println(result);
								String qtemp="select TABLE_NAME from INFORMATION_SCHEMA.TABLES";
								ArrayList<String> table_names= new ArrayList<String>();
								
								ResultSet rstemp=null;
								System.out.println("fetched tables");
								Statement stmt2 = conn.createStatement();

								if (stmt2.execute( qtemp)) {
									rstemp = stmt2.getResultSet();
					                                
								}
								if(rstemp!=null)
								{
									while(rstemp.next())
									{
								String table=rstemp.getString(1);
								table_names.add(table);
								System.out.println(table);
								
									}
								}
								int flag=0;
								System.out.println("Checking table exists or not");
								for (String table_temp:table_names)
								{
									System.out.println(table_temp);
									if(table_temp.equals(result))
									{
										
										System.out.println(table_temp);
										
										flag=1;
										break;
									}
								}
								if(flag==1)
								{
									System.out.println("table exists");
									continue;
									
								}
								else
								{
								String q_create="CREATE TABLE "+result+" ( primary_key varchar (100), ";
								
//								String q2="Select * from infoAttribute";
//								ResultSet rs2=null;
//								if (stmt.execute(q2 )) {
//									rs2 = stmt.getResultSet();
//					                                
//								}
//								if(rs2!=null)
//								{
//									while(rs2.next())
//									{
//										System.out.println(rs2.getString(1));
//										System.out.println(rs2.getString(2));
//										System.out.println(rs2.getString(3));
//										
//									}
//								}
								qtemp="Select count(attribute) from infoAttribute where p_info= ?";
								System.out.println("Executing query");
								PreparedStatement pst2 = conn.prepareStatement(qtemp);
								pst2.setString(1,result);
								int n=-1;
								
								ResultSet rcount=pst2.executeQuery();
								System.out.println("fetched result");
								if(rstemp!=null)
								{
									while(rcount.next())
									{
								n=rcount.getInt(1);
								System.out.println(n);
									}}
								int count=1;
								String q2="Select attribute, dataType from infoAttribute where p_info = ?";
								System.out.println("Executing query");
								PreparedStatement pst_4 = conn.prepareStatement(q2);
								pst_4.setString(1,result);
								
								ResultSet rs2=pst_4.executeQuery();
								System.out.println("fetched result");
								
								
									if(rs2!=null)
									{
										while(rs2.next())
										{
											System.out.println(rs2.getString(1));
											System.out.println(rs2.getString(2));
											
											if(count<n)
											{
											q_create=q_create+rs2.getString(1)+" "+rs2.getString(2)+" , ";
											}
											else
											{
												q_create=q_create+rs2.getString(1)+" "+rs2.getString(2)+" , PRIMARY KEY (primary_key))";
											}
											
											
											
											count++;
										}
									}
									System.out.println("Creating Fact table");
									System.out.println(result);
									Statement stmt_create = conn.createStatement();
									stmt_create.executeUpdate(q_create);
									System.out.println("Fact Table created");
									boolean flag2=createDimensions(result);
									System.out.println(flag2);
									
					                               
							}
							}
							boolean flag3=mapping();
							System.out.println("Mapping done");
							System.out.println(flag3);
							
						}
		}
						
		catch(Exception e)
		{
			e.printStackTrace();
			success=false;
		}
		
		return success;	
}
	public boolean createDimensions(String fact)
	{
		boolean success=true;
		System.out.println("CREATING TABLES FOR dimensions");
		
		String sql = null;
		ResultSet rs=null;
		try {
			Statement stmt = conn.createStatement();

						sql="USE "+db_name;
						stmt.executeUpdate(sql);
						

						sql = "Select category_name from category_subcategory where p_info = (?)";
						PreparedStatement pst_4 = conn.prepareStatement(sql);
						pst_4.setString(1,fact);
						
						ResultSet rs2=pst_4.executeQuery();
						System.out.println("fetched categories of a fact");
						if(rs2!=null)
						{ int count_fk_d=1;
							while (rs2.next()) {
								String result=rs2.getString(1);
			                                   
								System.out.println(result);
								System.out.println("fetching table names");
								String qtemp="select TABLE_NAME from INFORMATION_SCHEMA.TABLES";
								ArrayList<String> table_names= new ArrayList<String>();
								Statement stmt2 = conn.createStatement();
								ResultSet rstemp=null;
								if (stmt2.execute( qtemp)) {
									rstemp = stmt2.getResultSet();
					                                
								}
								System.out.println("fetched tables");
								if(rstemp!=null)
								{
									while(rstemp.next())
									{
								String table=rstemp.getString(1);
								table_names.add(table);
								
									}}
								int flag=0;
								for (String table: table_names)
								{
									if(table.equals(result))
									{
										flag=1;
										break;
									}
								}
								if(flag==1)
								{
									System.out.println("table exists");
									
								}
								else
								{
									System.out.println("starting create");
								String q_create="CREATE TABLE "+result+" ( primary_key varchar (100), ";
								
//								String q2="Select * from infoAttribute";
//								ResultSet rs2=null;
//								if (stmt.execute(q2 )) {
//									rs2 = stmt.getResultSet();
//					                                
//								}
//								if(rs2!=null)
//								{
//									while(rs2.next())
//									{
//										System.out.println(rs2.getString(1));
//										System.out.println(rs2.getString(2));
//										System.out.println(rs2.getString(3));
//										
//									}
//								}
								String qtemp2="Select count(DISTINCT attribute_name) from category_attributes where category_name= ?";
								System.out.println("fetching count");
								PreparedStatement pst2 = conn.prepareStatement(qtemp2);
								pst2.setString(1,result);
								int n=-1;
								
								ResultSet rstemp2=pst2.executeQuery();
								System.out.println("fetched count");
								if(rstemp2!=null)
								{
									while(rstemp2.next())
									{
								n=rstemp2.getInt(1);
								System.out.println(n);
									}}
								int count=1;
								System.out.println("fetched contents");
								String q2="Select DISTINCT attribute_name, dataType from category_attributes where category_name = ?";
								
								PreparedStatement pst3 = conn.prepareStatement(q2);
								pst3.setString(1,result);
								
								ResultSet rs_attr=pst3.executeQuery();
								System.out.println("fetched contents");
								
								
									if(rs_attr!=null)
									{
										while(rs_attr.next())
										{
											System.out.println(rs_attr.getString(1));
											System.out.println(rs_attr.getString(2));
											
											if(count<n)
											{
											q_create=q_create+rs_attr.getString(1)+" "+rs_attr.getString(2)+" , ";
											}
											else
											{
												q_create=q_create+rs_attr.getString(1)+" "+rs_attr.getString(2)+" , PRIMARY KEY (primary_key) )";
											}
											
											
											
											count++;
										}
									}
									
									System.out.println(q_create);
									System.out.println("Creating table");
									System.out.println(result);
									Statement stmt_create = conn.createStatement();
									stmt_create.executeUpdate(q_create);
									System.out.println("Tables Created");
									
									
									
									
									boolean flag3=createSubcategories(result);
									
									System.out.println(flag3);
									
					                               
							}
								String sub_check="Select category_name from category_subcategory where p_info= (?) and subcategory_of is NOT NULL";
								PreparedStatement pst_check=conn.prepareStatement(sub_check);
								pst_check.setString(1, fact);
								ArrayList<String> sub_cats=new ArrayList<String>();
								ResultSet rs_check=pst_check.executeQuery();
								if(rs_check!=null)
								{
									while(rs_check.next())
									{
										sub_cats.add(rs_check.getString(1));
									}
								}
								int flag_check=0;
								for (String tn:sub_cats)
								{
									if(tn.equals(result))
										{
											flag_check=1;
											break;
										}
								}
								if(flag_check!=1)
								{
								String count_fk_d_copy=Integer.toString(count_fk_d);
								String col_name="foreign_key"+count_fk_d_copy;
								String fk_fact="ALTER TABLE "+fact+" ADD "+col_name+" varchar(100)";
								System.out.println(fk_fact);
								Statement stmt_fact_fk = conn.createStatement();
								stmt_fact_fk.executeUpdate(fk_fact);
								String fk_const="ALTER TABLE "+fact+" ADD FOREIGN KEY ("+col_name+") REFERENCES "+result+" (primary_key)";
								System.out.println(fk_const);
								Statement stmt_fact_const = conn.createStatement();
								stmt_fact_const.executeUpdate(fk_const);
								System.out.println("Tables Altered");
								}
								
								count_fk_d++;
							}
							
							
						}
		}
						
		catch(Exception e)
		{
			e.printStackTrace();
			success=false;
		}
		
		return success;	
	}
	
	public boolean createSubcategories(String category)
	{
		boolean success=true;
		System.out.println("CREATING TABLES FOR subcategories");
		
		String sql = null;
		ResultSet rs=null;
		try {
			Statement stmt = conn.createStatement();

						sql="USE "+db_name;
						stmt.executeUpdate(sql);
						

						sql = "Select category_name from category_subcategory where subcategory_of = (?)";
						PreparedStatement pst_4 = conn.prepareStatement(sql);
						pst_4.setString(1,category);
						
						ResultSet rs2=pst_4.executeQuery();
						System.out.println("fetched sub-categories of a category");
						if(rs2!=null)
						{  	int count_fk=1;
							while (rs2.next()) {
								String result=rs2.getString(1);
			                                   
								System.out.println(result);
								System.out.println("fetching table names");
								String qtemp="select TABLE_NAME from INFORMATION_SCHEMA.TABLES";
								ArrayList<String> table_names= new ArrayList<String>();
								Statement stmt2 = conn.createStatement();
								ResultSet rstemp=null;
								if (stmt2.execute( qtemp)) {
									rstemp = stmt2.getResultSet();
					                                
								}
								System.out.println("fetched tables");
								if(rstemp!=null)
								{
									while(rstemp.next())
									{
								String table=rstemp.getString(1);
								table_names.add(table);
								
									}}
								int flag=0;
								for (String table: table_names)
								{
									if(table.equals(result))
									{
										flag=1;
										break;
									}
								}
								if(flag==1)
								{
									System.out.println("table exists");
									
									
								}
								else
								{
									System.out.println("starting create");
								
								
								String q_create="CREATE TABLE "+result+" ( primary_key varchar(100), ";
								
//								String q2="Select * from infoAttribute";
//								ResultSet rs2=null;
//								if (stmt.execute(q2 )) {
//									rs2 = stmt.getResultSet();
//					                                
//								}
//								if(rs2!=null)
//								{
//									while(rs2.next())
//									{
//										System.out.println(rs2.getString(1));
//										System.out.println(rs2.getString(2));
//										System.out.println(rs2.getString(3));
//										
//									}
//								}
								String qtemp2="Select count(DISTINCT attribute_name) from category_attributes where category_name= ?";
								System.out.println("fetching count");
								PreparedStatement pst2 = conn.prepareStatement(qtemp2);
								pst2.setString(1,result);
								int n=-1;
								
								ResultSet rstemp2=pst2.executeQuery();
								System.out.println("fetched count");
								if(rstemp2!=null)
								{
									while(rstemp2.next())
									{
								n=rstemp2.getInt(1);
								System.out.println(n);
									}}
								int count=1;
								System.out.println("fetched contents");
								String q2="Select DISTINCT attribute_name, dataType from category_attributes where category_name = ?";
								
								PreparedStatement pst3 = conn.prepareStatement(q2);
								pst3.setString(1,result);
								
								ResultSet rs_attr=pst3.executeQuery();
								System.out.println("fetched contents");
								
								
									if(rs_attr!=null)
									{
										while(rs_attr.next())
										{
											System.out.println(rs_attr.getString(1));
											System.out.println(rs_attr.getString(2));
											
											if(count<n)
											{
											q_create=q_create+rs_attr.getString(1)+" "+rs_attr.getString(2)+" , ";
											}
											else
											{
												q_create=q_create+rs_attr.getString(1)+" "+rs_attr.getString(2)+" , PRIMARY KEY (primary_key))";
											}
											
											
											
											count++;
										}
									}
									System.out.println(q_create);
									System.out.println("Creating table");
									System.out.println(result);
									Statement stmt_create = conn.createStatement();
									stmt_create.executeUpdate(q_create);
									System.out.println("Tables created");
									
									
					                               
							}
								String count_fk_copy=Integer.toString(count_fk);
								String col_name2="foreign_key"+count_fk_copy;
								String fk_cat="ALTER TABLE "+category+" ADD "+col_name2+" varchar(100)";
								System.out.println(fk_cat);
								Statement stmt_fk = conn.createStatement();
								stmt_fk.executeUpdate(fk_cat);
								
								String fk_cat_const="ALTER TABLE "+category+" ADD FOREIGN KEY ("+col_name2+") REFERENCES "+result+" (primary_key)";
								
								System.out.println(fk_cat_const);
								Statement stmt_cat_const = conn.createStatement();
								stmt_cat_const.executeUpdate(fk_cat_const);
								
								
								System.out.println("Tables Altered");
								
								
								
								count_fk++;
							}
							
							
						}
		}
						
		catch(Exception e)
		{
			e.printStackTrace();
			success=false;
		}
		
		return success;	
	}
	public boolean mapping()
	{
		boolean success=true;
		System.out.println("CREATING MAPPING TABLE");
		String sql = null;
		ResultSet rs=null;
		try {
			Statement stmt = conn.createStatement();

			sql="USE "+db_name;
			stmt.executeUpdate(sql);
			String qtemp="select TABLE_NAME from INFORMATION_SCHEMA.TABLES";
			ArrayList<String> table_names= new ArrayList<String>();
			Statement stmt2 = conn.createStatement();
			ResultSet rstemp=null;
			if (stmt2.execute( qtemp)) {
				rstemp = stmt2.getResultSet();
                                
			}
			System.out.println("fetched tables");
			if(rstemp!=null)
			{
				while(rstemp.next())
				{
			String table=rstemp.getString(1);
			table_names.add(table);
			
				}}
			int flag=0;
			for (String table: table_names)
			{
				if(table.equals("mapping"))
				{
					flag=1;
					System.out.println("mapping exists");
					break;
				}
			}
		if(flag!=1)
		{
			
			sql="CREATE TABLE mapping (fact varchar (100) NOT NULL, dimension varchar (100) NOT NULL, PRIMARY KEY (fact,dimension))";
			stmt.executeUpdate(sql);
			ResultSet dim_fact=null;
			sql = "Select DISTINCT p_info,category_name from category_subcategory";
			if (stmt.execute(sql )) {
				dim_fact = stmt.getResultSet();
                                
			}
			if(dim_fact!=null)
			{
				while(dim_fact.next())
				{
					String fact=dim_fact.getString(1);
					String dim=dim_fact.getString(2);
					
					java.sql.PreparedStatement pst;

					// insert in p_info table
					String q = "insert into mapping values (?,?)";
					pst= conn.prepareStatement(q); 
					pst.setString(1, fact);
					pst.setString(2, dim);
					pst.execute();
					
			}
			}
		}
		flag=0;
		for (String table: table_names)
		{
			if(table.equals("mapping2"))
			{
				flag=1;
				System.out.println("mapping2 exists");
				break;
			}
		}
		if(flag!=1)
		{
			sql="CREATE TABLE mapping2 (dimension varchar (100) NOT NULL, subdimension varchar (100) NOT NULL, PRIMARY KEY (dimension,subdimension))";
			stmt.executeUpdate(sql);
			ResultSet dim_subdim=null;
			sql = "Select DISTINCT subcategory_of,category_name from category_subcategory where subcategory_of IS NOT NULL";
			if (stmt.execute(sql )) {
				dim_subdim = stmt.getResultSet();
                                
			}
			if(dim_subdim!=null)
			{
				while(dim_subdim.next())
				{
					String dim=dim_subdim.getString(1);
					
					String subdim=dim_subdim.getString(2);
					
					
					
					java.sql.PreparedStatement pst;

					// insert in p_info table
					String q = "insert into mapping2 values (?,?)";
					pst= conn.prepareStatement(q); 
					pst.setString(1, dim);
					pst.setString(2, subdim);
					pst.execute();
					
					
			}
			}
		}
			
			
						

		}
						
		catch(Exception e)
		{
			e.printStackTrace();
			success=false;
		}
		
		return success;	
		
	}
	
	
}

