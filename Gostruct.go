// Unoptimized
// Language: go 
// link: https://towardsdev.com/golang-writing-memory-efficient-and-cpu-optimized-go-structs-62fcef4dbfd0
// [Golang] Writing memory efficient and CPU optimized Go Structs
package main

import (
	"fmt"
	"unsafe"
)

type TerraformResource struct {
	Cloud               string // 16 Bytes
	Name                string // 16 Bytes
	HaveDSL             bool   //  1 Byte
	PluginVersion       string // 16 Bytes
	IsVersionControlled bool   //  1 Byte
	TerraformVersion    string // 16 Bytes
	ModuleVersionMajor  int32  //  4 Bytes
}

func main() {
	var d TerraformResource
	d.Cloud = "aws"
	d.Name = "ec2"
	d.HaveDSL = true
	d.PluginVersion = "3.64"
	d.TerraformVersion = "1.1"
	d.ModuleVersionMajor = 1
	d.IsVersionControlled = true
	fmt.Println("==============================================================")
	fmt.Printf("Total Memory Usage StructType:d %T => [%d]\n", d, unsafe.Sizeof(d))
	fmt.Println("==============================================================")
	fmt.Printf("Cloud Field StructType:d.Cloud %T => [%d]\n", d.Cloud, unsafe.Sizeof(d.Cloud))
	fmt.Printf("Name Field StructType:d.Name %T => [%d]\n", d.Name, unsafe.Sizeof(d.Name))
	fmt.Printf("HaveDSL Field StructType:d.HaveDSL %T => [%d]\n", d.HaveDSL, unsafe.Sizeof(d.HaveDSL))
	fmt.Printf("PluginVersion Field StructType:d.PluginVersion %T => [%d]\n", d.PluginVersion, unsafe.Sizeof(d.PluginVersion))
	fmt.Printf("ModuleVersionMajor Field StructType:d.IsVersionControlled %T => [%d]\n", d.IsVersionControlled, unsafe.Sizeof(d.IsVersionControlled))
	fmt.Printf("TerraformVersion Field StructType:d.TerraformVersion %T => [%d]\n", d.TerraformVersion, unsafe.Sizeof(d.TerraformVersion))
	fmt.Printf("ModuleVersionMajor Field StructType:d.ModuleVersionMajor %T => [%d]\n", d.ModuleVersionMajor, unsafe.Sizeof(d.ModuleVersionMajor))
}
